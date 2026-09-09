# 8b Library

Public Reader, Explorer, and Guardian playground over the 8b.is document collection.

Website target: https://8b-is.github.io/8b-public-documents/

Hosting status: the source is public and the site is tested, but GitHub Actions is disabled for this repository by organization policy. A repository-level enable attempt returned HTTP409; organization-policy access returned HTTP403. An organization admin must allow Actions for this repository before the Pages workflow can execute. No organization policy was changed.

An offline build is available in the `library-2026-09-09` GitHub release. Unzip it, run `python3 -m http.server 8000 --bind 127.0.0.1` from the extracted folder, and open `http://127.0.0.1:8000/8b-public-documents/`.

## Run locally

Use Node 24 or newer. From `site/`:

```sh
npm ci
npm run dev
```

Open http://127.0.0.1:4321. Build with `npm run build`; output is `dist/`.
For the public project path:

```sh
SITE_URL=https://8b-is.github.io SITE_BASE=/8b-public-documents npm run build
SITE_BASE=/8b-public-documents npm run preview
```

## Content

- `../library/catalog.json` identifies the curated editions, authors, topics, relationships, sources, and checksums.
- `../library/readers/` contains derived full-text reading editions; preserved originals are in `../library/sources/`.
- `scripts/sync-library.mjs` checks and renders the curated catalog and copies downloads.
- `scripts/sync-docs.mjs` renders tracked legacy repository documents and copies their assets. It excludes private chats, instructions, tools, and the curated source tree.
- `src/content/docs/` contains hand-authored entry points. Generated pages are marked and recreated during sync. Do not edit generated copies.
- `../library-tools/` records the Marqant/Kompress fidelity trial. Lossy output does not replace reading editions.

## Verification

`npm test` exercises Guardian model boundaries and project-path handling.
Browser tests live under `tests/browser/`. After a production build:

```sh
npx playwright install chromium
SITE_BASE=/8b-public-documents npx playwright test
```

Playwright starts a local preview automatically. `SITE_BASE=/8b-public-documents python3 scripts/check-links.py` verifies all built page/download paths. CI runs both checks before publishing.
The model implements a declared subset of Guardian behavior, not a formal verification of AyeOS.

## Publish

Once permitted by organization policy, the `Publish 8b Library` workflow builds the static site and deploys it to GitHub
Pages on `main` changes or a manual run. No custom domain or running application
server is required. Set repository Pages source to GitHub Actions.

Authorship and individual reuse terms stay attached to works. No new blanket
license is assigned by ingestion. Private chat exports are not published.

To package a verified build: `python3 scripts/package-offline.py /tmp/8b-library-offline.zip`. The archive includes a source revision and a SHA-256 sidecar.
