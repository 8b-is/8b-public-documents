/**
 * MEMNET Library Semantic & Connected-Graph Retrieval Engine
 *
 * Replaces unranked flat substring matching with:
 *   1. Field-weighted relevance scoring (exact phrase, title, subtitle, topics,
 *      authors, summary, id)
 *   2. Connected-reading graph propagation (1-hop resonance bonus along
 *      `doc.related` edges when a neighbor strongly matches the query)
 *   3. Deterministic tie-breaking by score descending, then original catalog order.
 */

const FIELD_WEIGHTS = Object.freeze({
  exactPhraseTitle: 12.0,
  exactPhraseSummary: 6.0,
  titleTokenExact: 5.0,
  titleTokenPrefix: 3.5,
  subtitleToken: 3.0,
  topicExact: 4.5,
  topicPrefix: 2.5,
  authorToken: 3.0,
  summaryToken: 1.5,
  idToken: 2.5,
  connectedResonanceFactor: 0.25,
});

/**
 * Normalize and tokenize query or field text into lowercase alphanumeric terms.
 * Preserves hyphenated technical terms alongside their split components.
 */
export function tokenizeQuery(raw = '') {
  const cleaned = String(raw || '')
    .toLocaleLowerCase()
    .replace(/[’']/g, '')
    .trim();
  if (!cleaned) return [];
  return cleaned
    .split(/\s+/)
    .map(t => t.replace(/^[^a-z0-9-]+|[^a-z0-9-]+$/g, ''))
    .filter(Boolean);
}

function normalizeText(text = '') {
  return String(text || '')
    .toLocaleLowerCase()
    .replace(/[’']/g, '');
}

function splitWords(text = '') {
  return normalizeText(text)
    .split(/[^a-z0-9]+/)
    .filter(Boolean);
}

/**
 * Compute intrinsic field-weighted score for a single document against query terms.
 * Returns 0 if any required query term is completely absent from all fields of the document.
 */
export function scoreDocumentIntrinsic(doc, rawQuery = '') {
  const terms = tokenizeQuery(rawQuery);
  if (terms.length === 0) return 1.0;

  const titleNorm = normalizeText(doc.title);
  const subtitleNorm = normalizeText(doc.subtitle);
  const summaryNorm = normalizeText(doc.summary);
  const idNorm = normalizeText(doc.id);
  const topicsNorm = (doc.topics || []).map(normalizeText);
  const authorsNorm = (doc.authors || []).map(normalizeText);

  const titleWords = splitWords(doc.title);
  const subtitleWords = splitWords(doc.subtitle);
  const topicWords = topicsNorm.flatMap(splitWords);

  let totalScore = 0;
  const fullPhrase = terms.join(' ');

  if (terms.length > 1) {
    if (titleNorm.includes(fullPhrase) || subtitleNorm.includes(fullPhrase)) {
      totalScore += FIELD_WEIGHTS.exactPhraseTitle;
    } else if (summaryNorm.includes(fullPhrase)) {
      totalScore += FIELD_WEIGHTS.exactPhraseSummary;
    }
  }

  for (const term of terms) {
    let termScore = 0;

    if (titleWords.includes(term)) {
      termScore += FIELD_WEIGHTS.titleTokenExact;
    } else if (titleWords.some(w => w.startsWith(term)) || titleNorm.includes(term)) {
      termScore += FIELD_WEIGHTS.titleTokenPrefix;
    }

    if (subtitleWords.includes(term) || subtitleNorm.includes(term)) {
      termScore += FIELD_WEIGHTS.subtitleToken;
    }

    if (topicsNorm.includes(term) || topicWords.includes(term)) {
      termScore += FIELD_WEIGHTS.topicExact;
    } else if (topicsNorm.some(t => t.includes(term))) {
      termScore += FIELD_WEIGHTS.topicPrefix;
    }

    if (authorsNorm.some(a => a.includes(term))) {
      termScore += FIELD_WEIGHTS.authorToken;
    }

    if (summaryNorm.includes(term)) {
      termScore += FIELD_WEIGHTS.summaryToken;
    }

    if (idNorm.includes(term)) {
      termScore += FIELD_WEIGHTS.idToken;
    }

    // Strict conjunctive recall unless boosted via connected graph resonance
    if (termScore === 0) {
      return 0;
    }
    totalScore += termScore;
  }

  return Number(totalScore.toFixed(4));
}

/**
 * Retrieve and rank documents across the catalog using intrinsic field weights
 * plus 1-hop connected-reading (`related`) resonance.
 */
export function retrieveDocuments(documents, { query = '', topic = '', edition = '' } = {}) {
  const indexed = documents.map((doc, index) => ({
    doc,
    index,
    editionKind: doc.status === 'existing-collection' ? 'existing' : 'curated',
    intrinsicScore: scoreDocumentIntrinsic(doc, query),
  }));

  const byId = new Map();
  for (const entry of indexed) {
    if (entry.doc.id) {
      byId.set(entry.doc.id, entry);
    }
  }

  const hasQuery = tokenizeQuery(query).length > 0;

  const scored = indexed.map(entry => {
    const { doc, editionKind, intrinsicScore } = entry;
    if (topic && !(doc.topics || []).includes(topic)) {
      return { ...entry, score: 0, matched: false };
    }
    if (edition && editionKind !== edition) {
      return { ...entry, score: 0, matched: false };
    }
    if (!hasQuery) {
      return { ...entry, score: 1, matched: true };
    }
    if (intrinsicScore <= 0) {
      return { ...entry, score: 0, matched: false };
    }

    let resonanceBonus = 0;
    for (const relId of doc.related || []) {
      const neighbor = byId.get(relId);
      if (neighbor && neighbor.intrinsicScore > 0) {
        resonanceBonus += neighbor.intrinsicScore * FIELD_WEIGHTS.connectedResonanceFactor;
      }
    }

    const finalScore = Number((intrinsicScore + resonanceBonus).toFixed(4));
    return {
      ...entry,
      score: finalScore,
      matched: true,
    };
  });

  const matches = scored.filter(item => item.matched);
  if (hasQuery) {
    matches.sort((a, b) => b.score - a.score || a.index - b.index);
  }
  return matches;
}
