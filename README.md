# analiza-wydzwieku

# Charakterystyka projektu i zbioru danych:

Celem tego projektu jest przeprowadzenie analizy wydźwięku tweetów dotyczących aplikacji webowej "ChatGPT". Projekt wykorzystuje dane zebranie z Twittera. Analiza wydźwięku tweetów ma na celu zrozumienie nastrojów użytkowników Twittera wokół tematu "ChatGPT" oraz zobrazowanie tych nastrojów za pomocą odpowiednich wykresów. Aplikacja wykorzystuje bibliotekę TextBlob do analizy sentymentu tekstów oraz generuje wykresy, które wizualizują rozkład nastrojów i zmiany w czasie.
Ze względów technicznych program ogranicza się do 10000 pierwszych tweetow.

# Wykorzystane pliki CSV:

W ramach tego projektu wykorzystano plik CSV o nazwie "chatgpt.csv". Plik ten zawiera zbiór tweetów związanych z "ChatGPT" przez okres jednego miesiąca od uruchomienia. Każdy wiersz w pliku reprezentuje jeden tweet i zawiera informacje takie jak identyfikator tweeta, data utworzenia, liczba polubień, liczba cytatów, liczba odpowiedzi, liczba retweetów, treść tweeta, kraj, adres URL zdjęcia, miasto i kod kraju.

# Użyte biblioteki:

- pandas,
- textblob,
- matplotlib

# Wygenerowane wykresy:

W ramach tego projektu generowane są trzy wykresy, które wizualizują wyniki analizy nastrojów tweetów:

# Wykres słupkowy - "Distribution of Tweet Categories"

Ten wykres przedstawia rozkład kategorii tweetów na podstawie analizy sentymentu. Kategorie to pozytywne, neutralne i negatywne. Oś X reprezentuje poszczególne kategorie, a oś Y reprezentuje liczbę tweetów w każdej kategorii. Wykres ten pozwala zobaczyć, jakie kategorie dominują wśród tweetów związanych z aplikacją "ChatGPT".

![image](https://github.com/Al27Ms/analiza-wydzwieku-tweeta/assets/102626627/a2e4892b-16d5-4f98-821b-0c301262a387)

# Wykres słupkowy - "Distribution of Sentimentsin ChatGPT Tweets"

Ten wykres przedstawia rozkład nastrojów wśród tweetów związanych z aplikacją "ChatGPT". Wykorzystuje histogram, który dzieli zakres sentymentu na 10 równych przedziałów (bins). Oś X reprezentuje przedziały sentymentu, a oś Y reprezentuje liczbę tweetów w danym przedziale. Wykres ten pozwala zobaczyć, jakie nastroje dominują wśród tweetów - czy przeważają nastroje pozytywne, neutralne czy negatywne.

![image](https://github.com/Al27Ms/analiza-wydzwieku-tweeta/assets/102626627/4c6cec84-c6d3-45aa-9a9a-ecd48f337ace)

# Wykres liniowy - "Sentiment over Time in ChatGPT Tweets"

Ten wykres prezentuje zmiany w nastrojach tweetów związanych z aplikacją "ChatGPT" w czasie. Oś X reprezentuje czas, a oś Y reprezentuje wartość sentymentu. Dla każdego tweetu, wartość sentymentu jest odwzorowana na osi Y, a czas utworzenia tweeta jest odwzorowany na osi X. Wykres ten pozwala śledzić ewentualne zmiany w nastrojach wraz z upływem czasu i zidentyfikować trendy.

![image](https://github.com/Al27Ms/analiza-wydzwieku-tweeta/assets/102626627/752ec2af-a0b4-45e1-8025-4714f8301bef)

# Podsumowanie:

Projekt "Analiza Wydźwięku Tweetów" polegał na analizie nastrojów tweetów związanych z aplikacją "ChatGPT". Wykorzystano bibliotekę TextBlob do przeprowadzenia analizy sentymentu, generując wykresy przedstawiające rozkład kategorii, rozkład nastrojów oraz zmiany nastrojów w czasie. Projekt umożliwiał zrozumienie ogólnego nastroju użytkowników Twittera wokół aplikacji "ChatGPT" oraz identyfikację wzorców i tendencji.









