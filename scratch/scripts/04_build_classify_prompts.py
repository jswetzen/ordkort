"""Split the full word list into ~200-word batches per tier and write Fable classification prompts.

Output: classify/prompt_<tier>_<n>.md — each a self-contained prompt asking Fable to
independently verdict every word as good/bad and assign its correct tier, as pipe-delimited CSV.
"""
import json
import math
import os

with open("merged-clean.json", encoding="utf-8") as f:
    data = json.load(f)

HEADER = """Du granskar en ordlista for ett svenskt ordgissningsspel (Alias-stil): en spelare beskriver ett ord utan att saga det, laget gissar. Tre svarighetsgrader:

- enkelt: konkreta, vardagliga ord som barn och blandade grupper kan gissa direkt.
- mellan: mindre vardagliga men fortfarande beskrivbara ord for tonaringar/vuxna.
- svart: ord for vuxna som gillar en utmaning - men MASTE fortfarande vara riktiga, kanda svenska ord en beslast vuxen kanner igen NAR den hor en bra ledtrad. Inte ren fackjargong ingen kan ledtrada utan att redan kunna ordet.

Vi har redan granskat ett stickprov och hittat systematiska problem du ska leta efter har ocksa:
1. "mellan" laker nedat: massor av rena barnord (mat, djur, klader, vader, mobler) ligger felaktigt i mellan istallet for enkelt.
2. "svart" blandar ihop "abstrakt" med "svart": vardagsord som anvands dagligen (budget, symtom, perspektiv, kontrast, monster, adrenalin) har hamnat i svart bara for att de ar abstrakta begrepp - de hor hemma i mellan eller enkelt.
3. Ord som INTE fungerar i nagon niva ("bad", oavsett bakgrund):
   - "meta-ord" dar beskrivningen tvingar spelaren att sjalv saga malordet eller ett nastan-identiskt ord (t.ex. "ord" sjalvt).
   - utlandska varumarken/produktnamn som bara kan ledtradas som trivia (t.ex. specifika spritmarken).
   - rena facktermer/jargong som bara den som redan kan ordet forstar ledtraden pa.
   - fel grammatisk form (plural/bestamd form/genitiv dar grundform vore ratt), namn-forvaxlingsbara ord, eller ord vars dominanta betydelse ar nagot helt annat an det avsedda (stark homonymkrock).
   - felstavningar eller ord som inte ar riktig svenska.

For VARJE ord nedan, avgor sjalvstandigt (strunta i vilken niva ordet rakar ligga i just nu) och svara med EXAKT en rad per ord i detta format, med pipe-tecken | som separator, INGEN rubrikrad, INGEN markdown, INGEN kommentar utanfor raderna:

ord|verdikt|ratt_niva|motivering

dar:
- verdikt ar "good" eller "bad"
- ratt_niva ar "enkelt", "mellan" eller "svart" om verdikt=good (vilken niva ordet FAKTISKT hor hemma i), annars "cut" om verdikt=bad
- motivering ar MAX 6 ord, ingen pipe i motiveringen

Ord att klassificera (nuvarande niva: {tier}), {n} st:
{words}
"""

TIER_BATCHES = 2

os.makedirs("classify", exist_ok=True)
plan = []
for tier, words in data.items():
    n = len(words)
    batch_size = math.ceil(n / TIER_BATCHES)
    for i in range(TIER_BATCHES):
        chunk = words[i * batch_size:(i + 1) * batch_size]
        if not chunk:
            continue
        idx = i + 1
        fname = f"classify/prompt_{tier}_{idx}.md"
        prompt = HEADER.format(tier=tier, n=len(chunk), words=", ".join(chunk))
        with open(fname, "w", encoding="utf-8") as f:
            f.write(prompt)
        plan.append((tier, idx, len(chunk), fname))

for tier, idx, n, fname in plan:
    print(tier, idx, n, fname)
