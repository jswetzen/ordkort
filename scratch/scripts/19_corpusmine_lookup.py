import sys, json
freq = {}
with open('sv_full.txt', encoding='utf-8') as f:
    for line in f:
        parts = line.rstrip('\n').split(' ')
        if len(parts) != 2:
            continue
        w, c = parts
        try:
            c = int(c)
        except ValueError:
            continue
        # keep first occurrence (file sorted desc by freq, first is max, but should be unique anyway)
        if w not in freq:
            freq[w] = c

with open('topup2work/freq_all.json', 'w', encoding='utf-8') as f:
    json.dump(freq, f, ensure_ascii=False)
print(f"total unique words: {len(freq)}", file=sys.stderr)
