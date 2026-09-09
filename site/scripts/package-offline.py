#!/usr/bin/env python3
"""Package an already verified project-path build for offline serving."""
import argparse
import hashlib
import subprocess
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

parser = argparse.ArgumentParser()
parser.add_argument('output', type=Path)
args = parser.parse_args()
site = Path(__file__).resolve().parents[1]
dist = site / 'dist'
assert (dist / 'index.html').is_file(), 'Build the site first with SITE_BASE=/8b-public-documents'
revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=site, text=True).strip()
readme = '''8b Library — offline edition

Unzip this archive. In the extracted folder containing 8b-public-documents/,
run:

    python3 -m http.server 8000 --bind 127.0.0.1

Open http://127.0.0.1:8000/8b-public-documents/ in your browser.
The Reader, Explorer, local full-text search, and playground work without a
remote service. Optional web fonts can fall back to installed fonts. External
citations and project links require an internet connection.

Source PDFs, LaTeX, and Markdown are under 8b-public-documents/library/files/.
The catalog records edition hashes and attribution. Work-specific reuse terms
remain attached to each work. Private chat exports are not included.
'''
with ZipFile(args.output, 'w', compression=ZIP_DEFLATED, compresslevel=9) as archive:
    archive.writestr('README.txt', readme)
    archive.writestr('SOURCE_REVISION.txt', revision + '\n')
    for path in sorted(dist.rglob('*')):
        if path.is_symlink():
            raise SystemExit('Refusing symlink in build output')
        if path.is_file():
            archive.write(path, Path('8b-public-documents') / path.relative_to(dist))
digest = hashlib.sha256(args.output.read_bytes()).hexdigest()
args.output.with_suffix(args.output.suffix + '.sha256').write_text(f'{digest}  {args.output.name}\n')
print(f'Created {args.output.name}: {args.output.stat().st_size:,} bytes, SHA256 {digest}')
