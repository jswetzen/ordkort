rows = []
with open('topup2work/candidates_baseform_sorted.tsv', encoding='utf-8') as f:
    for line in f:
        w, c = line.rstrip('\n').split('\t')
        rows.append((w, int(c)))

suffixes = ['ism','itet','ation','tion','sion','ans','ens','else','dom','eri','skap',
            'logi','nomi','grafi','metri','krati','ur','tör','ör','ess','al','är','ös','iv','abel','ibel','and','ande']

by_suffix = {s: [] for s in suffixes}
for w, c in rows:
    for s in suffixes:
        if w.endswith(s) and len(w) >= len(s)+3:
            by_suffix[s].append((w,c))
            break

with open('topup2work/suffix_dump.txt', 'w', encoding='utf-8') as f:
    for s in suffixes:
        lst = sorted(by_suffix[s], key=lambda x: -x[1])
        f.write(f"=== -{s} ({len(lst)}) ===\n")
        for w, c in lst:
            f.write(f"{w}\t{c}\n")
        f.write("\n")
