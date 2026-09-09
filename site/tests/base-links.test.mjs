import test from 'node:test';
import assert from 'node:assert/strict';
import { withBase } from '../src/lib/base-links.mjs';
test('project deployment prefixes internal paths once and preserves external URLs', () => {
  assert.equal(withBase('/library/paper/#case', '/8b-public-documents/'), '/8b-public-documents/library/paper/#case');
  assert.equal(withBase('/8b-public-documents/library/', '/8b-public-documents'), '/8b-public-documents/library/');
  for (const value of ['https://example.com/', '//cdn.example.com/a', '#section', 'mailto:a@example.com']) assert.equal(withBase(value, '/8b-public-documents'), value);
  assert.equal(withBase('/library/', '/'), '/library/');
});
