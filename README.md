# Ordkort – ordgissningsspelet

En enkel, fristående webbversion av ett klassiskt ordgissningsspel, på svenska.
Tre svårighetsgrader (enkelt / mellan / svårt), ~1000 ord, inga upprepningar
förrän kortleken är slut.

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

## Köra lokalt

Det är en enda fristående HTML-fil utan byggsteg eller beroenden – öppna
`index.html` direkt i en webbläsare, eller servera mappen med valfri statisk
webbserver.

## Licens

MIT, se [LICENSE](LICENSE).
