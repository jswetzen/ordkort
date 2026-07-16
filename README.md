# Ordkort – ordgissningsspelet

En enkel, fristående webbversion av ett klassiskt ordgissningsspel, på svenska.
Tre svårighetsgrader (enkelt / mellan / svårt) plus ett bildläge för de minsta,
~1000 ord, inga upprepningar förrän kortleken är slut.

Öppna direkt: **https://jswetzen.github.io/ordkort/**

## Spela

1. Välj svårighetsgrad högst upp.
2. Tryck **Nytt ord** (eller mellanslag) för nästa ord.
3. Laget gissar utifrån ledtrådar utan att säga ordet självt, som i klassiska ordgissningsspel av det här slaget.

Ordkortet du sett sparas lokalt i webbläsaren (`localStorage`) så att samma ord
inte dyker upp igen förrän hela leken för den svårighetsgraden är slut. Knappen
"Nollställ alla kort" i sidfoten återställer alla tre leken.

## Om ordlistan

Orden är genererade och sedan validerade mot ett verkligt svenskt
frekvenskorpus ([hermitdave/FrequencyWords](https://github.com/hermitdave/FrequencyWords),
OpenSubtitles-baserat) för att sålla bort påhittade eller felstavade ord, samt
manuellt korrekturlästa för böjningsfel och dubbletter mellan nivåerna.

## Om bildläget

"Bilder" är ett fjärde läge tänkt för barn som ännu inte läser själva: 291 av
orden från Enkelt-nivån som går att avbilda entydigt som en enda bild (djur,
mat, fordon, vardagsföremål) har fått en ikon från [OpenMoji](https://openmoji.org)
(CC BY-SA 4.0), inbäddad direkt i sidan. Ord som är tvetydiga som bild (t.ex.
"ben" = arm/ben eller "hopp" = hopp/hopprep), abstrakta (t.ex. "kärlek",
"tävling") eller släktrelationer (t.ex. "farmor" vs "mormor") är exkluderade,
liksom dubbletter där flera ord skulle fått samma bild.

## Köra lokalt

Det är en enda fristående HTML-fil utan byggsteg eller beroenden – öppna
`index.html` direkt i en webbläsare, eller servera mappen med valfri statisk
webbserver.

## Licens

MIT, se [LICENSE](LICENSE).
