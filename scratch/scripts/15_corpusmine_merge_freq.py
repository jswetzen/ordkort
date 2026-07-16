freq = {}
with open('topup2work/candidates_raw.tsv', encoding='utf-8') as f:
    for line in f:
        w, c = line.rstrip('\n').split('\t')
        freq[w] = int(c)

base = [w.strip() for w in open('topup2work/candidates_baseform.txt', encoding='utf-8')]
rows = [(w, freq[w]) for w in base if w in freq]
rows.sort(key=lambda x: -x[1])
with open('topup2work/candidates_baseform_sorted.tsv', 'w', encoding='utf-8') as f:
    for w, c in rows:
        f.write(f"{w}\t{c}\n")
print(len(rows))
