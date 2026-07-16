"""Score a blind guesser's answers against the guess-test-key.json answer key, grouped by tier.

Input: guess-test-key.json, guesses-raw.json (index -> guessed word)
"""
import json

with open("guess-test-key.json", encoding="utf-8") as f:
    key = json.load(f)
with open("guesses-raw.json", encoding="utf-8") as f:
    guesses = json.load(f)

by_tier = {}
for idx, info in key.items():
    word = info["word"]
    tier = info["tier"]
    guess = guesses.get(idx, "")
    g = guess.strip().lower()
    w = word.strip().lower()
    g_stem = g.rstrip("na").rstrip("or").rstrip("er").rstrip("en").rstrip("n").rstrip("a")
    w_stem = w.rstrip("na").rstrip("or").rstrip("er").rstrip("en").rstrip("n").rstrip("a")
    if g == w:
        status = "EXACT"
    elif g_stem == w_stem and len(w_stem) > 2:
        status = "EXACT(infl)"
    else:
        status = "MISS"
    by_tier.setdefault(tier, []).append((word, guess, status))

for tier in ("enkelt", "mellan", "svart"):
    rows = by_tier.get(tier, [])
    n = len(rows)
    exact_n = sum(1 for _, _, s in rows if s.startswith("EXACT"))
    print(f"\n=== {tier} ({n} words, {exact_n} exact) ===")
    for word, guess, status in rows:
        marker = "OK " if status.startswith("EXACT") else "X  "
        print(f"  {marker}{word:15s} -> guessed: {guess}")
