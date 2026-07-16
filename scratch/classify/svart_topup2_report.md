# Svårt top-up round 2 — methodology report

**Output:** `classify/svart_topup2.json` — 168 words (target was 150–180).

## Method: corpus-mining, not free-generation

Nearly 100% of the final list was sourced by mining `sv_full.txt` directly — no
free-generation-then-verify step was needed, because the corpus-mining pass was
productive enough on its own. This directly targets the failure mode from the
Haiku batch (hallucinated suffixes, invented compounds): every word here is a
literal line from the corpus, so hallucination is structurally impossible.

Pipeline (scripts left in `topup2work/` for inspection):

1. `extract_candidates.py` — read all 904,474 lines of `sv_full.txt`, kept
   words matching `^[a-zåäö]+$`, with `2 <= freq <= 6000`, length >= 4, and
   not already in `classify/exclude_v2.json` / `classify/svart_current.json`.
   → 359,557 raw candidates.
2. Ran a Swedish hunspell dictionary check to drop non-words/typos/OCR noise
   → 213,800 survive.
3. Ran a stemmer and kept only words that are their own stem (i.e. already in
   base/dictionary form — filters out inflected duplicates like plurals or
   definite forms so each concept surfaces once) → 63,430 base-form candidates,
   sorted descending by frequency (`candidates_baseform_sorted.tsv`).
4. Bucketed that pool by suffix (`-ism`, `-itet`, `-ation/-tion/-sion`,
   `-ans/-ens`, `-else`, `-eri`, `-skap`, `-dom`, `-tör/-ör`, `-logi/-nomi/
   -grafi/-metri/-krati`, `-isk`, etc.) to make semantic review tractable —
   these are exactly the Latinate/academic derivational patterns that
   `good_examples.txt` shows are characteristic of genuine svårt words
   (abstraktion, dissonans, kontinuitet, modernism, ...).
5. Manually read every bucket, applied the svårt definition + family-friendly
   filter, and hand-picked candidates. This produced 394 vetted-good
   candidates — well above target, so a second curation pass trimmed to the
   strongest, most diverse 168 (see "Trimming" below). Every word was
   re-verified programmatically against `freq_all.json` (freq >= 2) and both
   exclude files immediately before writing the final JSON — zero failures.

No word in the final list required the free-generation-plus-verify fallback
(step 4 of the brief); the corpus yielded enough genuine material across every
requested domain that backfill wasn't necessary.

## Frequency band explored

Per-word frequency in the final 168: min 2, max 562, median 24.5, mean 58.7.
Distribution: 50 words at freq ≤10, 62 at 11–50, 44 at 51–200, 12 above 200
(max 562, for words like `arrogans`/`aggression`-type terms that are common in
written/formal registers but not spoken daily conversation).

This matches the calibration signal from `good_examples.txt`/`bad_examples.txt`:
frequency does NOT cleanly separate good/bad svårt words (e.g. good examples
`väsen` 779 and `syntes` 540 are *higher* frequency than several rejected
bad examples like `kontrast` 84 or `komposition` 83). So frequency was used
purely as a discovery mechanism (explore roughly the 2–600 band, occasionally
higher for words with strong semantic fit), never as a cutoff — every
inclusion/exclusion decision was made by reading the actual word and applying
the svårt test ("would most adults need this explained in daily conversation,
or only meet it in specific reading/professional contexts?").

## Trimming: 394 → 168

The suffix-bucket method over-produced relative to the 150–180 target
(394 candidates passed initial semantic screening). Rather than include all of
them, a second pass cut ~226 words to land in the target range, prioritizing:

- **Redundancy control**: where both a noun and its adjective/related form
  were candidates for the same concept (e.g. `excentricitet`/`excentrisk`,
  `dualism`/`dualitet`, `genialisk`/`genialitet`), kept only one.
- **Everyday-word risk**: cut anything that, on reflection, is used in
  ordinary daily talk more than the definition allows — e.g. `stabilitet`,
  `kompatibilitet`, `mobilitet` (modern social-mobility/tech jargon that's
  actually common now), `interaktion`, `distribution`, `dimension`,
  `precision` (all fairly everyday despite Latinate look — the same trap
  `bad_examples.txt` warns about).
- **Over-obscurity**: cut highly specialist/niche terms even when real words
  — e.g. `ekonometri`, `psykometri`, `homologi`, `fysionomi`,
  `historiografi`, most `-isk` demonym/nationality adjectives
  (`indisk`, `grekisk`, etc. — too basic anyway), and narrow taxonomic/clinical
  terms.
- **Sensitivity/family-friendliness**: excluded explicit-content-adjacent
  words (`koppleri`, `horeri`, `sutenör`, `obscenitet`, `perversion`,
  `promiskuitet`), heavy political/extremist terms (`nazism`, `fascism`,
  `rasism`, `terrorism`, `antisemitism` — real corpus words but wrong register
  for a party game), and words carrying disability/mental-illness stigma risk
  in casual Swedish usage (e.g. `spastisk`) or ethnicity/nationality terms with
  political sensitivity (`kurdisk`, `samisk`, `baskisk`, `saudisk`).
- **Domain balance**: kept a spread across science (`fysiologi`, `entropi`-
  adjacent chemistry/biology terms, `radioaktivitet`, `topologi`), economy
  (`volatilitet`, `soliditet`, `solvens`, `konsumtion`), law (`jurisdiktion`,
  `sanktion`, `restitution`, `forensisk`, `obduktion`), history/politics
  (`teokrati`, `aristokrati`, `meritokrati`, `koalition`, `totalitarism`),
  psychology (`hypokondrisk`, `klaustrofobisk`, `apatisk`, `narcissism`),
  arts (`kalligrafi`, `musikalitet`, `virtuositet`, `biografi`), and
  philosophy (`metafysisk`, `platonisk`, `stoisk`, `empirisk`, `truism`,
  `aforism`) — philosophy and science/academic-suffix words are the largest
  groups since that's where the corpus was richest for this register; arts is
  the thinnest category (4 words) but every domain requested has coverage.

## Judgment calls worth flagging

- `abstinens` and `obduktion` sit at the edge of "clinical/heavy" but were
  kept as neutral, non-graphic standard vocabulary (parallel to `insolvens`,
  `dissonans` already accepted in the existing good svårt set).
- A handful of words have two plausible senses where only one is the intended
  "svårt concept" (e.g. `patiens` = patience/card solitaire was cut instead,
  precisely because of that ambiguity risk for clue-giving).
- `resiliens` and `kryptisk`-type modern-buzzword candidates were mostly cut
  even when real and moderately uncommon, because they've become common in
  contemporary self-help/tech discourse — same "looks formal but is actually
  said constantly now" trap the brief warned about.
- All 168 words were spot-checked individually against the game's
  family-friendliness bar; nothing sexual, graphic, or extremist survived to
  the final list.

## Verification

Final list re-checked programmatically immediately before writing the JSON:
168/168 words have `freq >= 2` in `sv_full.txt`, 0/168 collide with
`classify/exclude_v2.json` or `classify/svart_current.json`, 0 duplicates
within the list itself.
