# Generate svårt word batch 1

model: haiku

---

You are generating words for a Swedish family party game (like Alias/charades): one player describes a word to teammates without saying it. This is tier SVÅRT (hard difficulty).

SVÅRT definition: abstract, societal, technical, or academic register; opaque compounds; or words whose definition is genuinely hard to produce on the spot. IMPORTANT: an average Swedish adult must still instantly recognize the word — hard means "hard to describe," NEVER "obscure." Reject anything a normal adult wouldn't already know. Examples already used elsewhere (do NOT repeat): nostalgi, ironi, algoritm, rättssäkerhet, medelklass, paradox, byråkrati, arrogans, demokrati.

Draw from a WIDE mix of domains: everyday emotions/psychology (avoid duplicates with above), science & nature phenomena, technology & internet culture, arts & aesthetics, sports/game strategy concepts, school/academic concepts, philosophy-lite everyday concepts, economy/work-life concepts, health/body abstract concepts, social dynamics. At most 3 words total from politics/ideology and at most 2 from religion — keep the large majority of the list non-political, common abstract vocabulary instead (things like "algoritm", "paradox", "ironi" style — recognizable, everyday-abstract, not academic jargon).

Hard rules:
1. Real, standard Swedish words that an ordinary adult clearly knows. Every single word will be checked against a large real-word frequency dictionary afterward, and anything not a genuine dictionary word — or anything so rare/jargon-y it barely appears in everyday Swedish — gets silently deleted. So there is ZERO benefit to inventing, misspelling, or padding with fabricated compounds/prefixes (like stringing together many "anti-" or invented "-ism" words) — it just gets thrown away. If you run out of strong genuine candidates, produce fewer rather than making things up. A shorter 100%-real list beats a padded fake/jargon one.
2. Single words/closed compounds only, lowercase, no spaces, no proper nouns/brand names/place names/people.
3. Family-friendly — no violent, sexual, or offensive content.
4. No two words may share the same root/prefix/stem pattern — max 2 words total across the whole list may share a stem (so NOT a cluster of anti-x or -ism words).
5. No duplicates. Grammatically pick ONE form of a word (not both adjective and noun form, e.g. pick "artificiell" OR a totally different word, not also "artificiellt").
6. Target is 150 words total but going a bit under is fine and expected — going over by inventing jargon/junk is NOT fine.

Output: use the Write tool to write ONLY this JSON (no markdown fences, no commentary) to:
/tmp/claude-1000/-home-johan-git-mikro-iac/39db4bbe-cd7f-4293-a6de-4ae6ec8dad7a/scratchpad/svart-batch-1.json

Format: {"words": ["ord1", "ord2", ...]}

After writing, your chat reply should just be one line reporting how many words you wrote. Do not paste the list back.