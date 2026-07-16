import sys

rows = []
with open('topup2work/candidates_baseform_sorted.tsv', encoding='utf-8') as f:
    for line in f:
        w, c = line.rstrip('\n').split('\t')
        rows.append((w, int(c)))

suffixes = ['ism','itet','ation','tion','sion','ans','ens','else','dom','eri','skap',
            'logi','nomi','grafi','metri','krati','arki','ur','it','esk','tris','tör',
            'age','ess','ör','and','ande','ende','ell','iell','al','är','ös','iv','abel','ibel']

by_suffix = {s: [] for s in suffixes}
for w, c in rows:
    for s in suffixes:
        if w.endswith(s) and len(w) >= len(s)+3:
            by_suffix[s].append((w,c))
            break  # only longest-matching... actually order matters, let's just pick first match in list order (already ordered longest-ish ok)

for s in suffixes:
    lst = by_suffix[s]
    print(f"{s}: {len(lst)}")
