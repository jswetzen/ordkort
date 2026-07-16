"""Fold the first top-up round's validated survivors into the exclusion list so the
next generation round doesn't re-propose them. Also report the current svart gap.

Foreign drink/brand names (ouzo, sake, grappa, vermouth, absint) are manually dropped
from the Fable-approved svart list here since Fable applied its own "no brand names"
rule inconsistently for these (see review/fable-review.md, which flagged "ouzo" as bad).
"""
import json

with open("merged-clean.json", encoding="utf-8") as f:
    original = json.load(f)
all_original = set()
for words in original.values():
    all_original.update(words)

with open("classify/fable_verdicts.json", encoding="utf-8") as f:
    verdicts = json.load(f)

DRINK_NAME_OVERRIDE_CUT = {"ouzo", "sake", "grappa", "vermouth", "absint"}
svart_good = [w for w in verdicts["new_tier"]["svart"] if w not in DRINK_NAME_OVERRIDE_CUT]

with open("topup/svart_validated.json", encoding="utf-8") as f:
    topup1 = json.load(f)
topup1_words = [w for w, _freq in topup1["survived"]]

current_svart = sorted(set(svart_good) | set(topup1_words))
print("svart good (post drink-name cut):", len(svart_good))
print("topup round 1 survivors:", len(topup1_words))
print("current svart total (deduped):", len(current_svart))
print("gap to 300:", max(0, 300 - len(current_svart)))

exclude_v2 = sorted(all_original | set(topup1_words))
print("\nupdated exclusion list size:", len(exclude_v2))

with open("classify/exclude_v2.json", "w", encoding="utf-8") as f:
    json.dump(exclude_v2, f, ensure_ascii=False, indent=2)

with open("classify/svart_current.json", "w", encoding="utf-8") as f:
    json.dump(current_svart, f, ensure_ascii=False, indent=2)
