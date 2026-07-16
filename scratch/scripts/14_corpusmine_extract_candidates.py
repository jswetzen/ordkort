import json, re, sys

# Load corpus
words = []
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
        words.append((w, c))

print(f"Total lines: {len(words)}", file=sys.stderr)

# Load exclusion set
excl = set(json.load(open('classify/exclude_v2.json')))
svart_current = set(json.load(open('classify/svart_current.json')))
excl |= svart_current
print(f"Exclude set size: {len(excl)}", file=sys.stderr)

pattern = re.compile(r'^[a-zåäö]+$')

MIN_FREQ = 2
MAX_FREQ = 6000
MIN_LEN = 4

candidates = []
for w, c in words:
    if not (MIN_FREQ <= c <= MAX_FREQ):
        continue
    if len(w) < MIN_LEN:
        continue
    if not pattern.match(w):
        continue
    if w in excl:
        continue
    candidates.append((w, c))

print(f"Candidates after freq/len/alpha/excl filter: {len(candidates)}", file=sys.stderr)

with open('topup2work/candidates_raw.tsv', 'w', encoding='utf-8') as f:
    for w, c in candidates:
        f.write(f"{w}\t{c}\n")
