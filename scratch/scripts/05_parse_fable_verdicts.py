"""Parse all Fable classification CSVs (classify/out_*.csv), sanity-check coverage against
the original word list, then compute the new tier composition and cut list.

Output: classify/fable_verdicts.json — {"new_tier": {tier: [words]}, "cut_words": [[word, old_tier, reason]]}
"""
import json
import glob
from collections import Counter, defaultdict

with open("merged-clean.json", encoding="utf-8") as f:
    original = json.load(f)

current_tier = {}
for tier, words in original.items():
    for w in words:
        current_tier[w] = tier

rows = []
for fname in sorted(glob.glob("classify/out_*.csv")):
    with open(fname, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line.strip():
                continue
            parts = line.split("|")
            if len(parts) != 4:
                print("MALFORMED in", fname, ":", repr(line))
                continue
            word, verdict, correct_tier, reason = [p.strip() for p in parts]
            rows.append((word, verdict, correct_tier, reason))

print("total classified rows (incl. any dupes):", len(rows))

# dedupe, keep first occurrence
seen = set()
uniq_rows = []
for r in rows:
    if r[0] in seen:
        continue
    seen.add(r[0])
    uniq_rows.append(r)
rows = uniq_rows

# coverage check vs original per-tier lists
orig_all = set()
for words in original.values():
    orig_all.update(words)
classified_words = set(w for w, _, _, _ in rows)
print("original unique words:", len(orig_all))
print("classified unique words:", len(classified_words))
print("missing from classification:", orig_all - classified_words)
print("extra (not in original):", classified_words - orig_all)

verdict_count = Counter(v for _, v, _, _ in rows)
print("\nverdict counts:", verdict_count)

new_tier = defaultdict(list)
cut_words = []
move_count = Counter()
for word, verdict, correct_tier, reason in rows:
    if verdict == "bad":
        cut_words.append((word, current_tier[word], reason))
    else:
        new_tier[correct_tier].append(word)
        if correct_tier != current_tier[word]:
            move_count[(current_tier[word], correct_tier)] += 1

print("\ncut words:", len(cut_words))
print("\nmoves (from -> to):", dict(move_count))

print("\nnew tier sizes after fable reclassification:")
for t in ("enkelt", "mellan", "svart"):
    print(" ", t, len(new_tier[t]), "-> gap to 300:", max(0, 300 - len(new_tier[t])))

with open("classify/fable_verdicts.json", "w", encoding="utf-8") as f:
    json.dump({"new_tier": new_tier, "cut_words": cut_words}, f, ensure_ascii=False, indent=2)
