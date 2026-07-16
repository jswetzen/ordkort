# Generate mellan word batch 1 (concrete-leaning domains)

model: haiku

---

You are generating words for a Swedish family party game (like Alias/charades): one player describes a word to teammates without saying it. This is tier MELLAN (medium difficulty).

MELLAN definition: known to most 10-year-olds and all adults, but not instantly obvious to a young child — either slightly abstract (an emotion, an activity concept), requires a bit of world knowledge (a profession, technology, a societal thing), or is concrete but lower-frequency. Describable in 1-2 plain sentences without specialist vocabulary. Examples already used elsewhere (do NOT repeat these, pick different words): avundsjuka, blogg, kompass, växthus, dirigent, skörd, ceremoni, framgång.

Cover ONLY these 10 domains for this batch, roughly evenly (~19 words each): djur (animals — pick less-common-but-still-known species/animal concepts, not the basic ones like hund/katt), mat & dryck, yrken, sport & lek, natur & växter, hushåll & möbler, verktyg & redskap, teknik & internet, känslor, verb & handlingar.

Hard rules:
1. Real, standard, everyday Swedish words ONLY. Every single word will be checked against a large real-word frequency dictionary afterward, and anything not a genuine dictionary word gets silently deleted. So there is ZERO benefit to inventing, misspelling, or padding with fabricated compounds — it just gets thrown away. If you run out of strong genuine candidates in a domain, produce fewer for that domain rather than making things up. A shorter 100%-real list beats a padded fake one.
2. Single words/closed compounds only, lowercase, no spaces, no proper nouns/brand names/place names/people.
3. Family-friendly (a child could draw this from a deck) — no violent, sexual, or offensive content.
4. No two words may share the same root/prefix/stem pattern (e.g. do not produce a cluster like näsdel/näsborr/näsrygg, or multiple "anti-" words) — max 2 words total across the whole list may share a stem.
5. No duplicates. Grammatically pick ONE form of a word (not both singular and plural, not both adjective and noun form).
6. Target is 190 words total but going a bit under is fine and expected — going over by inventing junk is NOT fine.

Output: use the Write tool to write ONLY this JSON (no markdown fences, no commentary) to:
/tmp/claude-1000/-home-johan-git-mikro-iac/39db4bbe-cd7f-4293-a6de-4ae6ec8dad7a/scratchpad/mellan-batch-1.json

Format: {"words": ["ord1", "ord2", ...]}

After writing, your chat reply should just be one line reporting how many words you wrote. Do not paste the list back.