import sys

words = [w.strip() for w in open('topup2work/candidates_hunspell_ok.txt', encoding='utf-8')]

blocks = []
current = []
with open('topup2work/candidates_stems.txt', encoding='utf-8') as f:
    for line in f:
        line = line.rstrip('\n')
        if line == '':
            blocks.append(current)
            current = []
        else:
            current.append(line)
    if current:
        blocks.append(current)

print(f"words: {len(words)} blocks: {len(blocks)}", file=sys.stderr)

# each block is list of lines like "word stem"
base_form_words = []
for w, block in zip(words, blocks):
    stems = set()
    for line in block:
        parts = line.split(' ')
        if len(parts) >= 2:
            stems.add(parts[1])
    if w in stems or not stems:
        base_form_words.append(w)

print(f"base form candidates: {len(base_form_words)}", file=sys.stderr)
with open('topup2work/candidates_baseform.txt', 'w', encoding='utf-8') as f:
    for w in base_form_words:
        f.write(w + '\n')
