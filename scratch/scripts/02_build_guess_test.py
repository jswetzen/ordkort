"""Shuffle Haiku-written clues, strip word/tier labels, and save the answer key separately.

Input: clues-raw.json (word -> clue), review-sample.json (tier -> [words])
Output: guess-test-key.json (index -> {word, tier, clue}), guess-test-clues-only.json (index -> clue)
"""
import json
import random

with open("clues-raw.json", encoding="utf-8") as f:
    clues = json.load(f)

with open("review-sample.json", encoding="utf-8") as f:
    sample = json.load(f)

word_to_tier = {}
for tier, words in sample.items():
    for w in words:
        word_to_tier[w] = tier

items = list(clues.items())
random.seed(7)
random.shuffle(items)

key = {}
numbered = {}
for i, (word, clue) in enumerate(items, start=1):
    key[i] = {"word": word, "tier": word_to_tier.get(word, "?"), "clue": clue}
    numbered[str(i)] = clue

with open("guess-test-key.json", "w", encoding="utf-8") as f:
    json.dump(key, f, ensure_ascii=False, indent=2)

with open("guess-test-clues-only.json", "w", encoding="utf-8") as f:
    json.dump(numbered, f, ensure_ascii=False, indent=2)

print(len(numbered), "clues written, key kept separately")
