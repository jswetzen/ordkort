"""Replace the embedded WORDS blob in ../index.html with the rebuilt final-wordlist.json.

Run from scratch/. Rewrites the single `var WORDS = {...};` line in place, leaving
everything else (styles, markup, script logic) untouched.
"""
import json
import re

with open("final-wordlist.json", encoding="utf-8") as f:
    words = json.load(f)

new_json = json.dumps(words, ensure_ascii=False, separators=(",", ":"))
new_line = f"  var WORDS = {new_json};"

path = "../index.html"
with open(path, encoding="utf-8") as f:
    content = f.read()

pattern = re.compile(r"^  var WORDS = \{.*\};$", re.MULTILINE)
matches = pattern.findall(content)
if len(matches) != 1:
    raise SystemExit(f"expected exactly 1 WORDS line, found {len(matches)}")

new_content = pattern.sub(lambda _: new_line.replace("\\", "\\\\"), content, count=1)

with open(path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("old WORDS line length:", len(matches[0]))
print("new WORDS line length:", len(new_line))
for tier in ("enkelt", "mellan", "svart"):
    print(tier, len(words[tier]))
