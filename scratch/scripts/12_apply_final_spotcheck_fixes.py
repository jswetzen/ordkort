"""Apply the 3 re-tier corrections surfaced by the closing Haiku-only spot check
(reviewer + blind-guess test both independently flagged these as too easy for svart):
profession, arkeologi, eufori -> move svart to mellan.
"""
import json

with open("final-wordlist.json", encoding="utf-8") as f:
    final = json.load(f)

MOVE_SVART_TO_MELLAN = {"profession", "arkeologi", "eufori"}

missing = MOVE_SVART_TO_MELLAN - set(final["svart"])
if missing:
    raise SystemExit(f"expected these in svart, not found: {missing}")

final["svart"] = [w for w in final["svart"] if w not in MOVE_SVART_TO_MELLAN]
final["mellan"] = sorted(set(final["mellan"]) | MOVE_SVART_TO_MELLAN)

for tier in ("enkelt", "mellan", "svart"):
    print(tier, len(final[tier]))
print("total:", sum(len(w) for w in final.values()))

with open("final-wordlist.json", "w", encoding="utf-8") as f:
    json.dump(final, f, ensure_ascii=False, indent=2)
