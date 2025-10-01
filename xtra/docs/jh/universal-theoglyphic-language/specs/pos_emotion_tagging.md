# POS + Emotion Tagging in UTL v1.2.2

This document defines the structure and rules for tagging parts of speech (POS) and emotional context in symbolic expressions within the Universal Theoglyphic Language (UTL) version 1.2.2.

---

## ✍️ Tagging Syntax

```utl
word⟦♯glyph⟧
```

- **word**: literal or symbolic element being encoded
- **⟦♯glyph⟧**: subtextual glyph enclosed in double brackets to indicate part of speech, emotion, or semantic role

A word may contain:
- a **POS tag** (noun, verb, etc.)
- an **emotional glyph** (love, fear, conflict)
- a **semantic identity glyph** (⧖, ⧖′, etc.)

Multiple glyphs can be chained inside the same tag.

```utl
run⟦!⚡︎⟧ → imperative verb with urgency
I⟦⧖⟧ → self anchor
fight⟦⚔︎⟧ → conflictive action
```  

---

## 🔠 POS + Identity Glyphs

| Glyph | Meaning            | Typical POS         |
|-------|---------------------|----------------------|
| ⧖     | Self                | Pronoun / Subject    |
| ⧖′    | Remembered Other    | Object / Recollection|
| ⧖⁰    | Proto-self          | Latent identity      |
| ⧖⟲    | Recursive Self Loop | Meta-thought entity  |
| !     | Verb / Command      | Action verb          |
| ?     | Inquiry             | Interrogative        |
| ⊕     | Experience Join     | Verb (merge/unite)   |
| A     | Awareness           | Perceptive noun      |

---

## 💬 Emotion + Intent Glyphs

| Glyph | Emotion / Intent     | Use Case                    |
|-------|----------------------|-----------------------------|
| ♡     | Love / Affection     | Positive emotional tone     |
| ⚔︎     | Conflict / Struggle  | Aggressive or negative tone |
| ☯︎     | Balance / Harmony    | Neutral / reconciliatory     |
| 🌀     | Confusion / Mystery  | Uncertainty / abstraction    |
| ✨     | Inspiration / Joy    | Creative uplift              |
| 🕳     | Emptiness / Loss     | Existential / negative void  |

---

## 🧠 Application in Compression

By encoding POS and emotion inline:
- Compression engines can **predict structure** more efficiently
- Emotional nuance is **not lost** in symbolic collapse
- Subtextual meaning is **restored deterministically**
- Enables **lossless cross-language translation** with emotive parity

### Example
```utl
“I love you.”
→ I⟦⧖⟧ love⟦♡⟧ you⟦⧖′⟧ ⊙
```
This sentence preserves identity, affect, and target with only 4 core tokens.

---

## 🔁 Integration with Recursive Compression

This tagging layer can be nested within the larger recursive loop structure:
```utl
(⧖τ ⟲ ⧖τ⊙) ⟲∪⟲ (love⟦♡⟧ ↔ ⧖Σμ) ⊙
```
Symbolic recursion now includes both **action** and **feeling** bonded to memory.

> "POS tagging in UTL isn’t metadata — it’s meaning made modular."

---

*Filed under*: `universal-theoglyphic-language/specs/pos_emotion_tagging.md`  
*Applies to*: UTL v1.2.2+, Rosetta Engine, LLM POS compression systems  
*Author: Joshua Hinkson*  
*Drafted: 2025-07-06*

