import fs from 'node:fs';
import { execFileSync } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const SITE_ROOT = path.resolve(__dirname, '..');
const REPO_ROOT = process.env.AYEVERSE_DOCS_ROOT ? path.resolve(process.env.AYEVERSE_DOCS_ROOT) : path.resolve(SITE_ROOT, '..');
const DOCS_DEST = path.join(SITE_ROOT, 'src/content/docs');
const FILES_DEST = path.join(SITE_ROOT, 'public/files');

const SKIP_DIRS = new Set([
  '.git',
  'library',
  'library-tools',
  'site',
  'node_modules',
  '.vscode',
  '.idea',
  'processing',
  'ortyx-project',
  'monograph',
  'preamble',
  'bibliography',
  'frontmatter',
  'appendices',
  'parts',
  'chapters',
]);

const SKIP_MD = new Set(['claude.md', 'agents.md', 'license', 'license.md']);

const ASSET_EXT = new Set([
  '.pdf',
  '.mp3',
  '.vtt',
  '.tex',
  '.txt',
  '.srt',
  '.tsv',
  '.png',
  '.jpg',
  '.jpeg',
  '.gif',
  '.webp',
  '.svg',
  '.json',
  '.wav',
  '.m4a',
  '.bib',
  '.fth',
]);

function walk(dir, acc = []) {
  let entries;
  try {
    entries = fs.readdirSync(dir, { withFileTypes: true });
  } catch {
    return acc;
  }
  for (const ent of entries) {
    if (ent.name.startsWith('.')) continue;
    const full = path.join(dir, ent.name);
    if (ent.isDirectory()) {
      if (SKIP_DIRS.has(ent.name)) continue;
      walk(full, acc);
    } else if (ent.isFile()) {
      acc.push(full);
    }
  }
  return acc;
}

function kebab(name) {
  return String(name)
    .replace(/_/g, '-')
    .replace(/([a-z0-9])([A-Z])/g, '$1-$2')
    .replace(/([A-Z]+)([A-Z][a-z])/g, '$1-$2')
    .replace(/[|_]/g, '-')
    .replace(/\s+/g, '-')
    .replace(/[^A-Za-z0-9.-]/g, '')
    .replace(/-+/g, '-')
    .toLowerCase();
}

function destMarkdownRel(rel) {
  const parsed = path.parse(rel);
  let base = parsed.name;
  const dir = parsed.dir;
  if (base.toUpperCase() === 'INDEX') base = 'catalog';
  if (base.toUpperCase() === 'README') {
    base = !dir || dir === '.' ? 'readme' : 'overview';
  }
  base = kebab(base);
  const outDir =
    !dir || dir === '.'
      ? ''
      : dir
          .split(path.sep)
          .map((seg) => kebab(seg))
          .join(path.sep);
  return path.join(outDir, `${base}.md`);
}

function titleFrom(content, fallback) {
  const h1 = content.match(/^#\s+(.+)$/m);
  if (h1) return h1[1].replace(/[#*_`]/g, '').trim();
  return fallback;
}

function descriptionFrom(content) {
  const fm = content.match(/^---\r?\n[\s\S]*?\r?\n---\r?\n/);
  let body = fm ? content.slice(fm[0].length) : content;
  body = body.replace(/^#\s+.*$/m, '');
  const para = body
    .split(/\n\s*\n/)
    .map((s) => s.trim())
    .find(
      (s) =>
        s &&
        !s.startsWith('#') &&
        !s.startsWith('```') &&
        !s.startsWith('|') &&
        !s.startsWith('<'),
    );
  if (!para) return '';
  return para.replace(/\s+/g, ' ').replace(/[#*_`>\[\]]/g, '').slice(0, 180);
}

function existingFrontmatter(content) {
  const m = content.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n/);
  if (!m) return { body: content };
  return { body: content.slice(m[0].length) };
}

function yamlQuote(s) {
  return `"${String(s).replace(/\\/g, '\\\\').replace(/"/g, '\\"').replace(/\n/g, ' ')}"`;
}

function rewriteLinks(body, fromFile, repoRoot) {
  const dir = path.dirname(fromFile);
  return body.replace(/(!?\[[^\]]*\]\()([^)\s]+)(\))/g, (all, pre, url, post) => {
    if (/^(https?:|mailto:|data:|#|\/)/i.test(url)) return all;
    const clean = url.split('#')[0].split('?')[0];
    const hash = url.includes('#') ? `#${url.split('#').slice(1).join('#')}` : '';
    let decoded = clean;
    try {
      decoded = decodeURIComponent(clean);
    } catch {
      decoded = clean;
    }
    const abs = path.resolve(dir, decoded);
    if (!fs.existsSync(abs)) return `${pre}https://github.com/8b-is/8b-public-documents/blob/main/${encodeURI(path.relative(repoRoot, abs).split(path.sep).join('/'))}${hash}${post}`;
    const rel = path.relative(repoRoot, abs);
    if (rel.startsWith('..')) return all;
    const ext = path.extname(decoded).toLowerCase();
    if (rel === 'library/catalog.json') return `${pre}/library/catalog.json${hash}${post}`;
    if (rel === 'site/README.md' || SKIP_MD.has(path.basename(rel).toLowerCase())) return `${pre}https://github.com/8b-is/8b-public-documents/blob/main/${encodeURI(rel)}${hash}${post}`;
    if (fs.statSync(abs).isDirectory() && fs.existsSync(path.join(abs, 'README.md'))) {
      const route = destMarkdownRel(path.join(rel, 'README.md')).replace(/\.md$/, '').split(path.sep).join('/');
      return `${pre}/${route}/${hash}${post}`;
    }
    if (fs.statSync(abs).isDirectory()) return `${pre}https://github.com/8b-is/8b-public-documents/tree/main/${encodeURI(rel)}${hash}${post}`;
    if (ASSET_EXT.has(ext)) {
      const web = `/files/${rel.split(path.sep).join('/')}`;
      return `${pre}${encodeURI(web)}${hash}${post}`;
    }
    if (ext === '.md' || ext === '.mdx') {
      const destRel = destMarkdownRel(rel).split(path.sep).join('/');
      return `${pre}/${destRel.replace(/\.md$/, '')}/${hash}${post}`;
    }
    return all;
  });
}

function cleanGenerated(dir) {
  if (!fs.existsSync(dir)) return;
  for (const f of walk(dir)) {
    if (!f.endsWith('.md') && !f.endsWith('.mdx')) continue;
    const txt = fs.readFileSync(f, 'utf8');
    if (txt.includes('ayeverse-sync') || txt.includes('ayeverse_sync')) fs.unlinkSync(f);
  }
}

function ensureDir(p) {
  fs.mkdirSync(p, { recursive: true });
}

cleanGenerated(DOCS_DEST);
ensureDir(DOCS_DEST);
fs.rmSync(FILES_DEST, { recursive: true, force: true });
ensureDir(FILES_DEST);

const tracked = new Set(execFileSync('git', ['ls-files', '-z'], { cwd: REPO_ROOT, encoding: 'utf8' }).split('\0'));
const files = walk(REPO_ROOT).filter(f => tracked.has(path.relative(REPO_ROOT, f)));
const catalog = [];
let pages = 0;
let assets = 0;

for (const full of files) {
  const rel = path.relative(REPO_ROOT, full);
  const ext = path.extname(full).toLowerCase();
  const base = path.basename(full);

  if (SKIP_MD.has(base.toLowerCase())) continue;

  if (ext === '.md' || ext === '.mdx') {
    const st = fs.statSync(full);
    if (st.size > 2_500_000) {
      console.warn('skip large md', rel);
      continue;
    }
    let raw = fs.readFileSync(full, 'utf8');
    if (raw.charCodeAt(0) === 0xfeff) raw = raw.slice(1);
    const { body: origBody } = existingFrontmatter(raw);
    let body = rewriteLinks(origBody, full, REPO_ROOT);
    const title = titleFrom(raw, path.parse(full).name.replace(/_/g, ' '));
    const description = descriptionFrom(raw);
    const destRel = destMarkdownRel(rel);
    const dest = path.join(DOCS_DEST, destRel);
    if (fs.existsSync(dest)) {
      const existing = fs.readFileSync(dest, 'utf8');
      if (!existing.includes('ayeverse-sync')) {
        console.log('keep hand-authored', destRel);
        continue;
      }
    }
    const front = [
      '---',
      `title: ${yamlQuote(title)}`,
      description ? `description: ${yamlQuote(description)}` : null,
      '---',
      '',
      '<!-- ayeverse-sync -->',
      '',
    ]
          .filter((x) => x !== null)
      .join('\n');
    ensureDir(path.dirname(dest));
    fs.writeFileSync(dest, front + body);
    catalog.push({ id: destRel.slice(0, -3).split(path.sep).join('/'), title, summary: description, reader: '/' + destRel.slice(0, -3).split(path.sep).join('/') + '/', topics: [rel.includes('/') ? rel.split('/')[0] : 'Overview'], kind: 'document', status: 'existing-collection', authors: [], source: rel });
    pages += 1;
  } else if (ASSET_EXT.has(ext)) {
    const st = fs.statSync(full);
    if (st.size > 80_000_000) {
      console.warn('skip huge asset', rel);
      continue;
    }
    const dest = path.join(FILES_DEST, rel);
    ensureDir(path.dirname(dest));
    fs.copyFileSync(full, dest);
    assets += 1;
  }
}

console.log(`Synced ${pages} pages, ${assets} assets → ${path.relative(REPO_ROOT, DOCS_DEST)}`);

// Give PDF-only papers an entry point and catalog record, even when no web text exists yet.
for (const full of files.filter(file => path.extname(file).toLowerCase() === '.pdf')) {
  const rel = path.relative(REPO_ROOT, full);
  const stem = rel.slice(0, -4);
  if (files.some(file => path.relative(REPO_ROOT, file).toLowerCase() === (stem + '.md').toLowerCase())) continue;
  const id = 'editions/' + stem.split(path.sep).map(kebab).join('/');
  const title = path.basename(stem).replace(/[_-]/g, ' ');
  const siblings = files.filter(file => path.relative(REPO_ROOT, file).slice(0, -path.extname(file).length) === stem && ASSET_EXT.has(path.extname(file).toLowerCase()));
  const links = siblings.map(file => {
    const relative = path.relative(REPO_ROOT, file).split(path.sep).join('/');
    return `- [${path.extname(file).slice(1).toUpperCase()}](/files/${encodeURI(relative)})`;
  }).join('\n');
  const body = `---\ntitle: ${yamlQuote(title)}\ndescription: "Preserved PDF edition from the existing collection."\n---\n\n<!-- ayeverse-sync -->\n\nThis edition is preserved from the existing repository collection. It has not received the September editorial review. Authorship and reuse terms remain those of the source work.\n\n${links}\n\nA web text edition may not yet be available. PDF accessibility varies across the legacy collection.\n`;
  const destination = path.join(DOCS_DEST, id + '.md');
  ensureDir(path.dirname(destination));
  fs.writeFileSync(destination, body);
  catalog.push({ id, title, summary: 'Preserved PDF edition with available source downloads.', reader: '/' + id + '/', topics: [rel.includes('/') ? rel.split('/')[0] : 'Overview'], kind: 'paper', status: 'existing-collection', authors: [], source: rel });
}

fs.writeFileSync(path.join(SITE_ROOT, 'public', 'collection-catalog.json'), JSON.stringify({ documents: catalog }, null, 2) + '\n');
