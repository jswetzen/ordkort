"""Shuffle the final-round clues, strip word/tier labels, and save the answer key
separately, for a blind guessability test on the rebuilt word list."""
import json
import random

with open("review/final-clues-raw.json", encoding="utf-8") as f:
    clues = json.load(f)

with open("review/final-review-sample.json", encoding="utf-8") as f:
    sample = json.load(f)

word_to_tier = {}
for tier, words in sample.items():
    for w in words:
        word_to_tier[w] = tier

items = list(clues.items())
random.seed(13)
random.shuffle(items)

key = {}
numbered = {}
for i, (word, clue) in enumerate(items, start=1):
    key[i] = {"word": word, "tier": word_to_tier.get(word, "?"), "clue": clue}
    numbered[str(i)] = clue

with open("review/final-guess-test-key.json", "w", encoding="utf-8") as f:
    json.dump(key, f, ensure_ascii=False, indent=2)

with open("review/final-guess-test-clues-only.json", "w", encoding="utf-8") as f:
    json.dump(numbered, f, ensure_ascii=False, indent=2)

print(len(numbered), "clues written, key kept separately")
