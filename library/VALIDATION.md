# Ingestion validation — 9 September 2026

The curated ingestion contains **six readers** and **17 downloadable artifacts**:
five source/PDF pairs, the original illustration, and six Markdown readers.

Completed checks:

- All 17 artifact sizes and SHA-256 digests match the catalog.
- Source and reader bibliography counts match: 11 entries for *Unknown Is Not
  Don't-Care*, seven for *Commitment Before Appearance*, and six for *The
  Verification Boundary*. All 25 citation targets link to retained entries.
- All five manuscript abstracts are present in the reader editions.
- All 166 inline/display mathematical expressions in the reader bodies render
  with the site's KaTeX dependency without a parse error.
- The Rust code block in the fixed-point reader matches its LaTeX source exactly.
- Both Guardian tables retain their headers and rows as Markdown tables.
- All five PDFs open successfully: seven, seven, four, seven, and 16 pages for
  Guardian, vocabulary, fixed point, commitment, and verification respectively.
- Public text and metadata contain no local user/workspace paths or chat exports.
- The illustration has descriptive alternative text, a full transcription, and a
  separately labeled editorial interpretation; attribution remains qualified.

The automatic catalog checks are repeatable with:

```sh
node site/scripts/sync-library.mjs --check
```

These are ingestion and rendering checks. They do not establish the empirical
claims in a manuscript or execute the Guardian verification proposal. The site
build and browser checks are recorded with the site implementation.
