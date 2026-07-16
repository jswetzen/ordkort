"""Merge Fable's reclassified enkelt/mellan tiers with the fully rebuilt svart tier
(Fable-approved core + two validated top-up rounds) into the final shipped word list.

Output: final-wordlist.json — {"enkelt": [...], "mellan": [...], "svart": [...]}
"""
import json

with open("classify/fable_verdicts.json", encoding="utf-8") as f:
    verdicts = json.load(f)

DRINK_NAME_OVERRIDE_CUT = {"ouzo", "sake", "grappa", "vermouth", "absint"}

enkelt = sorted(verdicts["new_tier"]["enkelt"])
mellan = sorted(verdicts["new_tier"]["mellan"])
svart_core = [w for w in verdicts["new_tier"]["svart"] if w not in DRINK_NAME_OVERRIDE_CUT]

with open("topup/svart_validated.json", encoding="utf-8") as f:
    topup1 = [w for w, _freq in json.load(f)["survived"]]

with open("classify/svart_topup2.json", encoding="utf-8") as f:
    topup2 = json.load(f)["words"]

svart_raw = set(svart_core) | set(topup1) | set(topup2)

# Priority enkelt > mellan > svart: the top-up rounds only excluded the ORIGINAL
# word list, not Fable's post-reclassification enkelt/mellan sets, so a top-up
# candidate can collide with a word Fable already placed in an easier tier
# (e.g. "mystik" was Haiku-proposed for svart but Fable had already classified
# it as mellan). Drop those collisions from svart rather than duplicate them.
enkelt_set, mellan_set = set(enkelt), set(mellan)
svart = sorted(svart_raw - enkelt_set - mellan_set)
dropped_as_easier_tier_dupe = sorted(svart_raw & (enkelt_set | mellan_set))
if dropped_as_easier_tier_dupe:
    print("dropped from svart (already in an easier tier):", dropped_as_easier_tier_dupe)

final = {"enkelt": enkelt, "mellan": mellan, "svart": svart}

# sanity: no word in more than one tier
seen = {}
dupes = []
for tier, words in final.items():
    for w in words:
        if w in seen:
            dupes.append((w, seen[w], tier))
        seen[w] = tier
print("cross-tier duplicates:", dupes)

for tier, words in final.items():
    print(tier, len(words))
print("total:", sum(len(w) for w in final.values()))

with open("final-wordlist.json", "w", encoding="utf-8") as f:
    json.dump(final, f, ensure_ascii=False, indent=2)
