# Curated library

This collection preserves five complete manuscripts and one supplied illustration,
with a full web reader for each. The first three papers are the reviewed editions
of 9 September 2026. *Commitment Before Appearance* and *The Verification Boundary*
remain unedited companion manuscripts. The image received via Nate retains its
original bytes; its transcription and editorial interpretation are separate.

## Source and reader layers

- `sources/<id>/` holds the exact supplied LaTeX, PDF, or image.
- `readers/<id>.md` holds complete accessible reader content. Mathematical notation,
  bibliography entries, footnotes, and the two Guardian tables are retained.
- `catalog.json` records identity, authorship, edition status, topics, related works,
  evidence limits, rights notes, and SHA-256 digests for every downloadable file.
- `tools/convert-readers.py` regenerates the five paper readers from LaTeX using
  Pandoc. The hand-transcribed illustration reader is maintained separately.

The catalog is the source for Reader and Explorer. Its URL paths are independent
of the deployment prefix. The site sync script adds `SITE_BASE` when rendering
links for a subdirectory deployment such as GitHub Pages.

The manuscript authors retain their attribution. No work-specific redistribution
license was supplied; this collection does not assign the repository's software
license to the included works. The figure's creator and original publication
source remain unverified. Private correspondence and local source locations are
excluded from the public collection.

## Build and validate

From the repository root:

```sh
node site/scripts/sync-library.mjs --check
node site/scripts/sync-library.mjs
```

Both `site/src/content/docs/library/` and `site/public/library/` are exclusively
generated. After validation succeeds, sync replaces their contents, including
stale pages and downloads from removed catalog entries. Keep hand-authored site
pages outside those directories. Generated directories and pages carry markers.
`--check` validates without writing any files and cannot be combined with
`--refresh-hashes`.

Normal site builds require Node.js and the site's existing dependencies. They use
the checked-in readers and PDFs, so Pandoc and a TeX engine are not required.

To regenerate readers after deliberately editing a canonical LaTeX manuscript:

```sh
python3 library/tools/convert-readers.py
# Review the full text, equations, citations, and any changed tables first.
node site/scripts/sync-library.mjs --refresh-hashes
node site/scripts/sync-library.mjs --check
```

The converter was run with Pandoc 3.11. It adapts the constructs used by this
collection; it is not a general-purpose LaTeX publication engine. New manuscripts
need an explicit conversion review. Refreshing hashes records approved bytes;
it does not establish the factual accuracy of a manuscript.

LaTeX and PDF are paired supplied artifacts. Rebuild a PDF when its LaTeX changes
and record the new edition; an unchanged old PDF must not silently be presented
as the rendering of new source. The three reviewed PDFs were previously built
with Tectonic 0.17.0, while the companion PDFs are the supplied editions.

## Adding a document

1. Preserve the source file and its supplied attribution under a stable new ID.
2. Create a full reader, keeping transcription distinct from interpretation and
   summaries distinct from source text.
3. Add the catalog entry with specific edition, evidence, and rights notes.
4. Review citation links, equations, tables, mobile layout, and keyboard access.
5. Refresh the reviewed file hashes and run the site checks and build.

Compression and retrieval derivatives must remain separate from these canonical
sources. The trials under `../library-tools/` measure tool behavior without
substituting a compressed summary for a reader or source manuscript.
