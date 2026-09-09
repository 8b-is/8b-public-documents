#!/usr/bin/env python3
"""Check local page/download links in a completed static build."""
import json
import os
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

root = Path(__file__).resolve().parents[1] / 'dist'
base = os.environ.get('SITE_BASE', '').rstrip('/')

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('href', 'src') and value:
                self.links.append(value)

missing = {}
pages = list(root.rglob('*.html'))
assert pages, 'Build the site first'
for page in pages:
    parser = Links()
    parser.feed(page.read_text())
    for link in parser.links:
        url = urlparse(link)
        if url.scheme or url.netloc or not url.path:
            continue
        path = unquote(url.path)
        if base and path.startswith(base + '/'):
            path = path[len(base):]
        elif base and path.startswith('/'):
            missing.setdefault(link, []).append(str(page.relative_to(root)))
            continue
        target = root / path.lstrip('/') if path.startswith('/') else page.parent / path
        if target.is_dir():
            target /= 'index.html'
        if not target.exists():
            missing.setdefault(link, []).append(str(page.relative_to(root)))
if missing:
    raise SystemExit(json.dumps(missing, indent=2))
print(f'Validated page and download paths across {len(pages)} HTML pages.')
