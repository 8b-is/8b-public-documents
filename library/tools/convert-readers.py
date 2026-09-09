#!/usr/bin/env python3
"""Regenerate full reader bodies with Pandoc; retain canonical LaTeX unchanged.

Requires Pandoc 3.11 or compatible. Only known constructs in this curated set
are adapted. A newly curated paper must be reviewed before publishing its reader.
"""
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def convert(source: Path) -> str:
    text = source.read_text()
    # Flatten print hierarchy (part -> section, its sections/subsections ->
    # subsection) so the web outline never skips heading levels.
    if r"\part" in text:
        text = re.sub(r"(?m)^\\section\{", r"\\subsection{", text)
        text = text.replace(r"\part*{", r"\section*{")
    # Pandoc treats abstract and thebibliography as metadata/unsupported raw
    # content by default. Make both visible, with resolvable citation links.
    text = text.replace(r"\begin{abstract}", r"\section*{Abstract}")
    text = text.replace(r"\end{abstract}", "")
    bibliography = re.findall(r"\\bibitem\{([^}]+)\}", text)

    def citation(match):
        links = []
        for key in match[1].split(","):
            number = bibliography.index(key.strip()) + 1
            links.append(r"\href{#reference-" + str(number) + "}{[" + str(number) + "]}")
        return ", ".join(links)

    text = re.sub(r"\\cite\{([^}]+)\}", citation, text)
    text = re.sub(r"\\begin\{thebibliography\}\{[^}]+\}", r"\\section*{References}", text)
    text = text.replace(r"\end{thebibliography}", "")
    text = re.sub(r"\\bibitem\{([^}]+)\}",
                  lambda match: r"\subsection*{Reference " + str(bibliography.index(match[1]) + 1) + "}", text)

    # Preserve table cell semantics while removing print-only column widths.
    text = text.replace(r"\begin{tabularx}{\textwidth}{@{}YY@{}}", r"\begin{tabular}{ll}")
    text = text.replace(r"\begin{tabularx}{\textwidth}{@{}>{\RaggedRight\arraybackslash}p{0.25\textwidth}YY@{}}", r"\begin{tabular}{lll}")
    text = text.replace(r"\end{tabularx}", r"\end{tabular}")
    text = text.replace(r"\begin{center}", "").replace(r"\end{center}", "")
    for environment in ("definition", "principle"):
        counter = 0

        def environment_title(match):
            nonlocal counter
            counter += 1
            return r"\textbf{" + environment.title() + " " + str(counter) + " (" + match[1] + ").}"

        text = re.sub(r"\\begin\{" + environment + r"\}\[([^\]]+)\]", environment_title, text)
        text = text.replace(r"\end{" + environment + "}", "")

    text = text.replace(r"\ref{sec:experiment}",
                        r"\href{#a-bounded-experiment-not-a-full-system-proof}{4.2}")
    text = text.replace(r"\begin{lstlisting}", r"\begin{lstlisting}[language=rust]")
    result = subprocess.run([
        "pandoc", "--from=latex", "--to=gfm-tex_math_gfm+tex_math_dollars+footnotes",
        "--wrap=none", "--shift-heading-level-by=1",
    ], input=text, text=True, capture_output=True, check=True)
    if result.stderr.strip():
        raise RuntimeError(result.stderr)
    markdown = result.stdout
    # Display mathematics must be isolated for remark-math (including one-line
    # equations, which Pandoc's GFM writer otherwise keeps between inline $$).
    markdown = re.sub(r"\$\$(.*?)\$\$", lambda match: "\n\n$$\n" + match[1].strip() + "\n$$\n\n", markdown, flags=re.S)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    # Remove incidental one-space tails introduced before display equations.
    # Keep any deliberate Markdown hard breaks (two trailing spaces) intact.
    markdown = "\n".join(line if line.endswith("  ") else line.rstrip(" \t")
                         for line in markdown.splitlines())
    return markdown.strip() + "\n"


if __name__ == "__main__":
    for source in sorted((ROOT / "sources").glob("*/*.tex")):
        target = ROOT / "readers" / (source.stem + ".md")
        target.write_text(convert(source))
        print(f"Converted {source.stem}")
