# Calibrate Swedish Alias word difficulty

model: fable

---

We're building a Swedish-language word-guessing party game (like "Alias" / charades-with-words), rendered as a single web page. Players pick a difficulty tier — Enkelt (easy), Mellan (medium), Svårt (hard) — and get one random Swedish word at a time to describe to teammates without saying the word itself.

Your job right now is NOT to produce the final word list (that bulk work happens later, by another model). Your job is to build calibrated judgment about what separates the three tiers, by actually trying it on real words, and then to write a tight few-shot prompt that will be handed verbatim to another AI to bulk-generate ~1000 classified Swedish words.

Do this:
1. Pick ~20 real Swedish words spanning a wide range: everyday concrete nouns (hund, bord, sked), everyday actions (springa, sova), kid-familiar things (glass, boll, saga), professions (brandman, tandläkare), nature/animals (ekorre, igelkott), household/tools (hammare, brevlåda), abstract/emotion words (avundsjuka, nostalgi), compound or tricky words (medelklass, rättssäkerhet), loanwords/tech (algoritm, blogg), pop-culture-adjacent but not brand-specific concepts, idiomatic/hard-to-mime abstractions (paradox, ironi). For each, reason through: would a 6-8 year old know and recognize this instantly (Enkelt)? Is it common but needs a bit more vocabulary/world knowledge or is a bit less concrete (Mellan)? Is it abstract, rare, a compound, or genuinely hard to describe/mime without saying the word (Svårt)?
2. From that exercise, distill explicit, checkable criteria per tier (concreteness, word frequency in everyday Swedish, syllable/compound complexity, whether a young child would know it, describability without gestures-only, cultural/domain specificity).
3. Decide a sensible tier split for a ~1000-word master list (e.g. roughly how many Enkelt vs Mellan vs Svårt makes sense for a family game where the easy tier is used heavily by kids) and say why.
4. List ~15-20 semantic domains to sample from for diversity (djur, mat, yrken, sport, natur, hushåll, teknik, känslor, verb/handlingar, platser, kroppsdelar, fordon, väder, färger, verktyg, abstrakta begrepp, skolan, kläder, musik/instrument, etc.) so the bulk generator doesn't produce a narrow/repetitive list.
5. Write the final deliverable: a self-contained few-shot prompt (in English instructions is fine, but the example words/tiers should be Swedish) that includes: the tier definitions, ~5-8 concrete example words per tier with one-line justification each, the domain list, explicit rules to avoid duplicates/proper nouns/brand names/offensive content/multi-word phrases (single words or very short compounds only, no full sentences), and an output format spec (I will tell it to output JSON — just make sure your prompt states words must be lowercase Swedish, one word/compound per entry, tier label attached).

Output: your reasoning can be brief, but end your response with a clearly delimited final section titled "FEWSHOT PROMPT" containing the complete prompt text ready to paste into another model's instructions. Keep total response under ~700 words excluding the delimited prompt section.