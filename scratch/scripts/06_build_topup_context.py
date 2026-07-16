"""Build the exclusion list (every word already in the game) and good/bad calibration
examples used in the svart top-up generation prompts.

Output: classify/exclude_all_original.json, topup/exclude_str.txt, topup/good_examples.txt, topup/bad_examples.txt
"""
import json
import os

with open("merged-clean.json", encoding="utf-8") as f:
    original = json.load(f)

all_original = set()
for words in original.values():
    all_original.update(words)

os.makedirs("classify", exist_ok=True)
os.makedirs("topup", exist_ok=True)

with open("classify/exclude_all_original.json", "w", encoding="utf-8") as f:
    json.dump(sorted(all_original), f, ensure_ascii=False)

with open("classify/fable_verdicts.json", encoding="utf-8") as f:
    v = json.load(f)

print("all_original count:", len(all_original))
print("svart good words (Fable-approved), n=", len(v["new_tier"]["svart"]))

exclude_str = ", ".join(sorted(all_original))

# Curated from classify/fable_verdicts.json's svart list, with foreign drink/brand
# names manually removed (ouzo/sake/grappa/vermouth/absint) since Fable applied its
# own "no foreign product names" rule inconsistently for these.
good_examples = ['abstraktion', 'arketyp', 'assimilation', 'asymmetri', 'cynism', 'deflation', 'dissonans',
                  'distorsion', 'emotion', 'entropi', 'essens', 'etymologi', 'högmod', 'insolvens', 'klassicism',
                  'kontinuitet', 'melankoli', 'metamorfos', 'missämja', 'modernism', 'momentum', 'narrativ',
                  'nepotism', 'notarie', 'oligarki', 'perception', 'projektion', 'resonans', 'retorik',
                  'sediment', 'semantik', 'singularitet', 'synaps', 'syntax', 'syntes', 'tonalitet',
                  'tribalism', 'vasall', 'vemod', 'värdighet', 'väsen', 'vånda']

bad_examples_too_easy = ['kristall', 'metall', 'kod', 'virus', 'stil', 'försvar', 'reflex', 'mönster', 'humor',
                          'bevis', 'fakta', 'vinst', 'allergi', 'kaos', 'vibration', 'fossil', 'komet', 'smak',
                          'budget', 'symtom', 'perspektiv', 'kontrast', 'adrenalin', 'atmosfär', 'prestige',
                          'komposition', 'strategi', 'myt', 'sensation']

with open("topup/exclude_str.txt", "w", encoding="utf-8") as f:
    f.write(exclude_str)
with open("topup/good_examples.txt", "w", encoding="utf-8") as f:
    f.write(", ".join(good_examples))
with open("topup/bad_examples.txt", "w", encoding="utf-8") as f:
    f.write(", ".join(bad_examples_too_easy))

print("exclude chars:", len(exclude_str))
