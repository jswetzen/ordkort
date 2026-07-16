import json

freq = {}
with open("sv_full.txt", encoding="utf-8") as f:
    for line in f:
        parts = line.rstrip("\n").split(" ")
        if len(parts) != 2:
            continue
        w, c = parts
        try:
            freq[w] = int(c)
        except ValueError:
            continue

with open("topup/svart_new_1.json", encoding="utf-8") as f:
    b1 = json.load(f)["words"]
with open("topup/svart_new_2.json", encoding="utf-8") as f:
    b2 = json.load(f)["words"]

with open("classify/exclude_all_original.json", encoding="utf-8") as f:
    exclude = set(json.load(f))

all_candidates = list(dict.fromkeys(b1 + b2))
print("total unique candidates:", len(all_candidates))
print("overlap with exclude list:", set(all_candidates) & exclude)

MINFREQ = 2
survived = []
rejected = []
for w in all_candidates:
    fr = freq.get(w.lower(), 0)
    if fr >= MINFREQ:
        survived.append((w, fr))
    else:
        rejected.append((w, fr))

print("survived:", len(survived))
print("rejected:", len(rejected))

with open("topup/svart_validated.json", "w", encoding="utf-8") as f:
    json.dump({"survived": survived, "rejected": rejected}, f, ensure_ascii=False, indent=2)
