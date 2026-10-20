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

## Read the curated works

| Work | Reading edition | Preserved download |
| --- | --- | --- |
| Unknown Is Not Don’t-Care | [Markdown](readers/unknown-not-dontcare.md) | [PDF](sources/unknown-not-dontcare/unknown-not-dontcare.pdf) |
| From Vocabulary to Kernel | [Markdown](readers/vocabulary-to-kernel.md) | [PDF](sources/vocabulary-to-kernel/vocabulary-to-kernel.pdf) |
| Two Meanings of Fixed Point | [Markdown](readers/fixed-point-essay.md) | [PDF](sources/fixed-point-essay/fixed-point-essay.pdf) |
| Commitment Before Appearance | [Markdown](readers/commitment-before-appearance.md) | [PDF](sources/commitment-before-appearance/commitment-before-appearance.pdf) |
| The Verification Boundary | [Markdown](readers/verification-boundary.md) | [PDF](sources/verification-boundary/verification-boundary.pdf) |
| Field Before Spike | [Transcription and notes](readers/field-before-spike.md) | [Original image](sources/field-before-spike/field-before-spike.jpg) |

Web-specific links in the reader Markdown target the library website. Use the
PDF/source links above while hosting is pending, or download the offline site
from the repository’s Releases page.

## Sovereign Library & Constellation Ontology Bridges

This library's core epistemic commitments — **`Compression ≠ Ontology`** and **[Unknown Is Not Don’t-Care](readers/unknown-not-dontcare.md)** across [The Verification Boundary](readers/verification-boundary.md) — anchor the wider `8b-is` / `vaked.dev` constellation ontology:

- **Verification Invariant (`+1* → 0 → +1`):** A plausible or compressed branch (`+1*`) may be ranked, never silently bound; an unobserved interval (`0`) must remain honestly open rather than collapsed into Don’t-Care or false certainty; only a provenance- and witness-verified branch (`+1`) may be bound.
- **`8b-is/sovereign-library` ([`ONTOLOGY.md`](https://github.com/8b-is/sovereign-library/blob/main/ONTOLOGY.md) & [`SOURCES.md`](https://github.com/8b-is/sovereign-library/blob/main/SOURCES.md)):**
  - Enforces the constitutional print-canon invariant (`Five books, never more`, `PRINTABLE = HELD ∧ READ`, `NAND(1,1) = 0`), pairing `the-nand-book.md`, `readability-is-freedom.md`, `purple-people-eaters.txt`, `admissible-degradation.txt`, and the linked `diatribe` corpus with the source garden (`standardgalactic/memnet` as the *Residue of Proof* & 8b Library reader lane).
  - Holds **Ultralove Editions 001–004** beside the five-book shelf:
    - **001:** *YOUR NAME — my favourite anime depth* (`editions/ultralove/your-name.md`)
    - **002:** *In Awe to Women Who Protect and Hold `<3<3<3`* (`editions/ultralove/women-who-protect-and-hold.md` — the Six Pillars of Holding: `Compassion ↔ Moderation`, `Understanding ↔ Respect`, `Love ↔ Space`)
    - **003:** *Dragon Ball Sovereign Ontology* (the Four-Fold Balanced-Ternary Matrix `{-1, 0, +1}`)
    - **004:** *Wigle-Triad v2.0.0 & Sanctuary Resonance* (`8b-is/wigle-triad v2.0.0`: `Boldog Még` `{<3,<3,<3}+1` + `ALEX|qMom` `.oOo. Poo .oOo.` box-bondage diagnostic + 432 Hz Shinjuku Gyoen Crickets & Drone Zone)
- **`8b-is/fandom-mcp` (`fandom_sovereign_ontology`):**
  - The 9-tool Dragon Ball Universe Scouter & Sovereign Ontology MCP server ([`8b-is/fandom-mcp`](https://github.com/8b-is/fandom-mcp), featuring `fandom_dbz_scouter`, `fandom_dbz_saga`, and `fandom_sovereign_ontology`) maps the balanced-ternary registers directly onto `memnet`'s verification boundary:
    - **`-1` (Trap / Bondage):** Architect / Ma-rigpa / Scalar Scouter Trap (mistaking compressed scalar numbers for living phase) / Box Bondage (`.oOo. Poo .oOo.`)
    - **`0` (Stillness / Honest Unknown):** Dharmakāya / Śūnyatā (*Mūlamadhyamakakārikā 24:18*) / *Unknown Is Not Don’t-Care* (`NAND(1,1) = 0`) / Ultra Instinct Stillness / 432 Hz Shinjuku Gyoen Crickets & Drone Zone
    - **`+1` (Verified / Bound):** Sambhogakāya–Nirmāṇakāya (`Inner E=mc²` & Clear Light `Ösel`) / Six Pillars of Holding / Shenron & Family Hearth (`{<3,<3,<3}+1` · `Boldog Még`)
- **Interactive Omni Book (`pocoo.vaked.dev`):**
  - Live reader and ontology bridge at [`https://pocoo.vaked.dev/demos/book/dragon-ball-sovereign-ontology-omni.html`](https://pocoo.vaked.dev/demos/book/dragon-ball-sovereign-ontology-omni.html).
