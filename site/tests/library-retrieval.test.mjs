import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import { retrieveDocuments, scoreDocumentIntrinsic } from '../src/lib/library-retrieval.mjs';

const curatedCatalog = JSON.parse(
  fs.readFileSync(new URL('../../library/catalog.json', import.meta.url), 'utf8')
);
const legacyUrl = new URL('../public/collection-catalog.json', import.meta.url);
const legacyCatalog = fs.existsSync(legacyUrl)
  ? JSON.parse(fs.readFileSync(legacyUrl, 'utf8'))
  : { documents: [] };
const allDocs = [...curatedCatalog.documents, ...legacyCatalog.documents];

test('field-weighted retrieval ranks exact title match above summary-only mentions', () => {
  const results = retrieveDocuments(allDocs, { query: 'From Vocabulary to Kernel' });
  assert.ok(results.length >= 1);
  assert.equal(results[0].doc.id, 'vocabulary-to-kernel');
  assert.ok(results[0].score > 20, `expected high phrase+title score, got ${results[0].score}`);
});

test('subtitle and smart-apostrophe normalization match "dont care" against "Unknown Is Not Don’t-Care"', () => {
  const results = retrieveDocuments(allDocs, { query: "dont-care state abstraction" });
  assert.ok(results.length >= 1);
  assert.equal(results[0].doc.id, 'unknown-not-dontcare');
});

test('connected-reading resonance boosts documents linked to strongly matching neighbors', () => {
  const synthetic = [
    {
      id: 'isolated-doc',
      title: 'Memory Notes',
      subtitle: '',
      summary: 'A short note on memory and guardian checks.',
      topics: ['Memory'],
      authors: ['Flyxion'],
      related: [],
      status: 'revised-draft',
    },
    {
      id: 'hub-doc',
      title: 'Memory Notes',
      subtitle: '',
      summary: 'A short note on memory and guardian checks.',
      topics: ['Memory'],
      authors: ['Flyxion'],
      related: ['guardian-anchor'],
      status: 'revised-draft',
    },
    {
      id: 'guardian-anchor',
      title: 'Guardian Memory Architecture',
      subtitle: 'Formal Guardian Verification',
      summary: 'Deep guardian memory verification.',
      topics: ['Guardian', 'Memory'],
      authors: ['Flyxion'],
      related: ['hub-doc'],
      status: 'revised-draft',
    },
  ];

  const intrinsicIsolated = scoreDocumentIntrinsic(synthetic[0], 'guardian memory');
  const intrinsicHub = scoreDocumentIntrinsic(synthetic[1], 'guardian memory');
  assert.equal(intrinsicIsolated, intrinsicHub);

  const ranked = retrieveDocuments(synthetic, { query: 'guardian memory' });
  assert.equal(ranked.length, 3);
  assert.equal(ranked[0].doc.id, 'guardian-anchor');
  assert.equal(ranked[1].doc.id, 'hub-doc');
  assert.equal(ranked[2].doc.id, 'isolated-doc');
  assert.ok(ranked[1].score > ranked[2].score);
});

test('topic and edition filters compose cleanly with ranked retrieval', () => {
  const curatedGuardian = retrieveDocuments(allDocs, {
    query: 'guardian',
    topic: 'Guardian',
    edition: 'curated',
  });
  assert.ok(curatedGuardian.length > 0);
  for (const item of curatedGuardian) {
    assert.ok(item.doc.topics.includes('Guardian'));
    assert.notEqual(item.doc.status, 'existing-collection');
  }
});
