# UTL Migrator (v1.1 → v1.3 symbolic translator)
# Author: Joshua Hinkson | Drafted: 2025-07-06

import re
import hashlib

# Internal cache for symbolic sentence patterns
structure_cache = {}


def generate_structure_id(structure: str) -> str:
    """Generates a symbolic ID for reuse of compressed structures."""
    hash_digest = hashlib.sha1(structure.encode("utf-8")).hexdigest()
    return f"🧾[{hash_digest[:3].upper()}]"


def migrate_legacy_UTL(text: str) -> str:
    """
    Transforms v1.1 UTL expressions into v1.3 symbolic equivalents,
    returning both the migrated output and symbolic structure cache ID.
    """
    if re.search(r"\(⟲.*?⊙\)", text):
        inner = re.findall(r"⟲(.*?)⊙", text)[0].strip()
        parts = inner.split()

        if len(parts) == 3:
            subj_raw, verb_raw, obj_raw = parts

            subj = f"{subj_raw}⟦⧖⟧"
            verb = f"{verb_raw}⟦♡!⟧" if verb_raw.lower() == "love" else f"{verb_raw}⟦!⟧"
            obj = f"{obj_raw}⟦⧖′⟧"

            # Build full structure
            full_structure = f"⌖SVO :: (⧖τ ⟲ ⧖τ⊙) ⟲∪⟲ ({verb} ↔ ⧖Σμ) {obj} ⊙"
            sid = generate_structure_id(full_structure)
            structure_cache[sid] = {
                "pattern": "⌖SVO",
                "components": {
                    "subject": subj,
                    "verb": verb,
                    "object": obj
                },
                "compressed": full_structure
            }
            return f"{sid}⟦⧖⟧  # compressed recall syntax"

        else:
            return f"(⧖τ ⟲ ⧖τ⊙) ⟲∪⟲ (Σ ↔ ⧖Σμ) ⊙  # legacy unstructured"

    return text  # passthrough


def print_cached_structure(sid: str):
    """Retrieves the compressed structure and components from cache."""
    return structure_cache.get(sid, {}).get("compressed", "[UNKNOWN STRUCTURE]")


# Example usage:
if __name__ == "__main__":
    example = "(⟲ I love you ⊙)"
    migrated = migrate_legacy_UTL(example)
    print("Legacy Input:", example)
    print("Migrated Output:", migrated)

    sid = migrated.split("⟦")[0]  # extract 🧾[XXX] ID
    expanded = print_cached_structure(sid)
    print("Expanded from Cache:", expanded)
