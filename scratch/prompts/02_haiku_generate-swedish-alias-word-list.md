# Generate Swedish Alias word list

model: haiku

---

You are generating a word list for a Swedish family party game (like Alias/charades-with-words): one player describes a Swedish word to teammates without saying the word itself. Generate words classified into three difficulty tiers.

## Tier definitions

ENKELT — A typical Swedish 6–8-year-old knows and recognizes this word instantly. Concrete things you can see, touch, or act out, or basic everyday actions. Describable in one plain sentence. Transparent kid-world compounds are fine (brandman, brevlåda).

MELLAN — Known to most 10-year-olds and all adults, but fails the Enkelt test in at least one way: slightly abstract (emotions, activity concepts), requires world knowledge (professions, technology, society), or concrete but lower-frequency. Describable in 1–2 sentences without specialist vocabulary.

SVÅRT — Abstract, societal, technical, or academic register; opaque compounds; or words whose definition is genuinely hard to produce on the spot. IMPORTANT: an average Swedish adult must still recognize the word — hard means "hard to describe," never "obscure." Do not use rare jargon, archaic words, or dictionary curiosities.

## Calibrated examples

ENKELT:
- hund — top-frequency, concrete, every child knows it
- glass — kid-favorite, instantly describable
- springa — basic action, easy to act out and describe
- boll — concrete toy, universal child vocabulary
- brandman — compound, but transparent and firmly in kid-world
- igelkott — longer word, but a concrete animal every child recognizes
- saga — kid-familiar from bedtime stories despite not being a physical object

MELLAN:
- avundsjuka — kids know the feeling, but the abstract noun form takes vocabulary to describe
- blogg — common loanword, requires internet world-knowledge
- kompass — concrete but lower-frequency; needs some world knowledge to explain
- växthus — transparent compound, yet outside a young child's active vocabulary
- dirigent — profession all adults know but few children could name
- skörd — common word, but abstract-ish process a 7-year-old would stall on

SVÅRT:
- nostalgi — abstract emotion in adult register, hard to pin down in words
- ironi — frequent word, but notoriously hard to define on the spot
- algoritm — recognized by all adults, crisply describable by few
- rättssäkerhet — opaque abstract compound, societal domain
- medelklass — abstract social concept despite familiar parts
- paradox — abstract loanword requiring an example to explain
- byråkrati — known to every adult, resists a one-sentence description

## Domain coverage

Sample broadly across ALL of these domains; do not let any domain exceed ~10% of the list:
djur, mat & dryck, yrken, sport & lek, natur & växter, hushåll & möbler, verktyg & redskap, teknik & internet, känslor, verb & handlingar, platser & byggnader, kroppsdelar, fordon & transport, väder & årstider, kläder, musik & instrument, skolan, familj & högtider, sagor & fantasi, abstrakta begrepp & samhälle.

Verbs should appear in every tier (Enkelt: hoppa; Mellan: övertala; Svårt: prefer abstract nouns for Svårt, verbs there should be rare).

## Rules

1. Standard Swedish words only. Established loanwords used in everyday Swedish are allowed (blogg, algoritm).
2. Single words only: one word or one closed compound per entry. No multi-word phrases, no sentences, no hyphenated novelties, no spaces in any entry.
3. All words lowercase.
4. No proper nouns, no brand names, no place names, no people.
5. No offensive, sexual, violent, political-figure, or otherwise family-unfriendly content. Everything must be safe for a child to draw from the deck.
6. No duplicates, and no near-duplicates: do not include both a word and its plural, definite form, or trivial derivation (hund vs hundar vs hunden; avundsjuk vs avundsjuka — pick one form only). No word may appear in more than one tier.
7. Every word must be describable in speech (not mime-only).

## Your task

Generate a list of EXACTLY these target counts:
- enkelt: 400 words
- mellan: 350 words
- svart: 250 words

(Total 1000. "svart" is the JSON key for svårt — plain ASCII, no å/ä/ö in the key name, but the Swedish words themselves DO use å/ä/ö normally, e.g. "häst", "sköldpadda", "körsbär" are all valid entries.)

Work through the domain list systematically for each tier so coverage is broad and not repetitive (don't just do 50 animals then stop — spread across all ~20 domains within each tier). Before finalizing, mentally scan your three lists for accidental duplicates (including across tiers) and fix them, and verify each tier's count is at or very near its target (within ~10 words is fine, exact is better).

## Output

Use the Write tool to write ONLY this JSON structure (no markdown fences, no commentary) to the file:
/tmp/claude-1000/-home-johan-git-mikro-iac/39db4bbe-cd7f-4293-a6de-4ae6ec8dad7a/scratchpad/alias-words.json

Format:
{"enkelt": ["ord1", "ord2", ...], "mellan": ["ord1", "ord2", ...], "svart": ["ord1", "ord2", ...]}

All words lowercase, double-quoted, comma-separated, valid JSON. After writing the file, your final chat response should be brief: just report the actual count you wrote for each tier. Do NOT paste the word lists back into your response.