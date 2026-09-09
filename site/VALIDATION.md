# Library release validation — 9 September 2026

- Production build: 137 HTML pages, including 127 catalog entries (121 existing collection entries and six newly curated works).
- Static link checker: no missing local page or download paths across all 137 pages under `/8b-public-documents`.
- Unit tests: 11 passing checks for project paths and Guardian boundaries, resets, saturation, and the terminal latch.
- Browser suite: all nine checks passed in the consolidated production run; they cover Pagefind full-text search, Explorer filters and persisted query state, keyboard-driven Guardian behavior, trace export, image/transcription availability, deployment paths, mobile layout, and reading without JavaScript.
- Automated axe checks cover the home page, Explorer, playground, and illustration Reader in light and dark themes against WCAG 2 A/AA and WCAG 2.1 AA tags. This is limited automated coverage, not a claim of complete accessibility certification.
- Curated ingestion: all 17 downloadable artifacts match catalog hashes; five PDFs open; 166 math expressions render; bibliography and citation counts are preserved. See `../library/VALIDATION.md`.
- Compression trial: 10 inputs, 69 evaluations, exact corpus hashes. See `../library-tools/README.md` for measured fidelity limits.
- Dependency audit after updating Astro, Starlight, and image tooling: zero reported vulnerabilities.

The playground is a declared subset of Guardian behavior. No exhaustive Guardian-versus-implementation trace exploration or new AyeOS runtime validation is claimed by this site release.

The CI workflow repeats the build, source validation, unit tests, static link check, and browser suite before publishing to GitHub Pages.
