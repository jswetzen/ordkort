"""Sample 20 random words per tier from the shipped word list for quality review."""
import json
import random

with open("merged-clean.json", encoding="utf-8") as f:
    data = json.load(f)

for tier in ("enkelt", "mellan", "svart"):
    print(tier, len(data[tier]))

random.seed(42)
sample = {tier: random.sample(data[tier], 20) for tier in ("enkelt", "mellan", "svart")}
with open("review-sample.json", "w", encoding="utf-8") as f:
    json.dump(sample, f, ensure_ascii=False, indent=2)

for tier, words in sample.items():
    print(f"\n{tier}:", ", ".join(words))
