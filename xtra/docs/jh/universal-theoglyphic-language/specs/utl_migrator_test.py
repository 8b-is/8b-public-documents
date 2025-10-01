# UTL Migrator Test Suite
# Tests cross-language symbolic rewrites from UTL v1.1 → v1.3

from utl_migrator import migrate_legacy_UTL, print_cached_structure

# Test phrases across multiple base languages
legacy_tests = {
    "English": "(⟲ I love you ⊙)",
    "Spanish": "(⟲ Yo amo tú ⊙)",
    "French": "(⟲ Je aime toi ⊙)",
    "German": "(⟲ Ich liebe dich ⊙)",
    "Portuguese": "(⟲ Eu amo você ⊙)",
    "Japanese (Romaji)": "(⟲ Watashi wa anata o aishiteimasu ⊙)",
    "Arabic (translit)": "(⟲ Ana uhibbuka ⊙)"
}

print("\n🔍 UTL MIGRATOR — v1.1 → v1.3 SYMBOLIC TESTS")

for lang, sentence in legacy_tests.items():
    migrated = migrate_legacy_UTL(sentence)
    sid = migrated.split("⟦")[0] if "⟦" in migrated else None
    expanded = print_cached_structure(sid) if sid else "[NON-STANDARD]"

    print(f"\n🌐 Language: {lang}")
    print(f"Legacy Input:    {sentence}")
    print(f"Migrated Output: {migrated}")
    print(f"Reconstructed:   {expanded}")
