"""Sample 20 random words per tier from the NEW final word list for the closing
Haiku-only verification pass (reviewer + clue-writer + blind-guesser)."""
import json
import random

with open("final-wordlist.json", encoding="utf-8") as f:
    data = json.load(f)

for tier in ("enkelt", "mellan", "svart"):
    print(tier, len(data[tier]))

random.seed(99)
sample = {tier: random.sample(data[tier], 20) for tier in ("enkelt", "mellan", "svart")}
with open("review/final-review-sample.json", "w", encoding="utf-8") as f:
    json.dump(sample, f, ensure_ascii=False, indent=2)

for tier, words in sample.items():
    print(f"\n{tier}:", ", ".join(words))
