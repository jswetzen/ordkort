# Generate svårt word batch 2

model: haiku

---

You are generating words for a Swedish family party game (like Alias/charades): one player describes a word to teammates without saying it. This is tier SVÅRT (hard difficulty).

SVÅRT definition: abstract, societal, technical, or academic register; opaque compounds; or words whose definition is genuinely hard to produce on the spot. IMPORTANT: an average Swedish adult must still instantly recognize the word — hard means "hard to describe," NEVER "obscure." Reject anything a normal adult wouldn't already know. Examples already used elsewhere (do NOT repeat): nostalgi, ironi, algoritm, rättssäkerhet, medelklass, paradox, byråkrati, arrogans, demokrati, metafor, symbolism, abstraktion.

Draw from a WIDE mix of domains, with a bias toward CONCRETE-domain words that are nonetheless hard to define/describe (this is different from batch 1 which focused on pure abstract nouns): things like specific hard-to-mime professions or specialized objects, nature/science phenomena that are familiar words but tricky to explain (e.g. gravitation-adjacent, weather/astronomy phenomena), body/health words that are known but hard to define crisply, historical-era concepts everyone knows the word for, emotions that are subtle/compound (not basic glad/ledsen), workplace/economy words, food/culture concepts that carry abstract meaning (e.g. a tradition, not a dish).

Hard rules:
1. Real, standard Swedish words that an ordinary adult clearly knows. Every single word will be checked against a large real-word frequency dictionary afterward, and anything not a genuine dictionary word — or anything so rare/jargon-y it barely appears in everyday Swedish — gets silently deleted. So there is ZERO benefit to inventing, misspelling, or padding with fabricated compounds/prefixes — it just gets thrown away. If you run out of strong genuine candidates, produce fewer rather than making things up. A shorter 100%-real list beats a padded fake/jargon one.
2. Single words/closed compounds only, lowercase, no spaces, no proper nouns/brand names/place names/people.
3. Family-friendly — no violent, sexual, or offensive content.
4. No two words may share the same root/prefix/stem pattern — max 2 words total across the whole list may share a stem.
5. No duplicates. Grammatically pick ONE form of a word (not both adjective and noun form).
6. Target is 150 words total but going a bit under is fine and expected — going over by inventing jargon/junk is NOT fine.

Output: use the Write tool to write ONLY this JSON (no markdown fences, no commentary) to:
/tmp/claude-1000/-home-johan-git-mikro-iac/39db4bbe-cd7f-4293-a6de-4ae6ec8dad7a/scratchpad/svart-batch-2.json

Format: {"words": ["ord1", "ord2", ...]}

After writing, your chat reply should just be one line reporting how many words you wrote. Do not paste the list back.