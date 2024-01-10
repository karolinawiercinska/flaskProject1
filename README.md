Dokumentacja aplikacji DELEGA 
zrealizowanej w ramach zajęć 
Inżynierii oprogramowania 
w semestrze letnim roku akademickiego 
2023/2024



Sopot, 2024 
Charakterystyka oprogramowania
Nazwa skrócona: DELEGA
Pełna nazwa:
Krótki opis ze wskazaniem celów: Aplikacja DELEGA to prosty kalkulator online, który umożliwia szybkie obliczanie szacunkowych kosztów podróży służbowych.
Link do repozytorium: https://github.com/karolinawiercinska/flaskProject1

Prawa autorskie

Autorzy:

Sylwia Bukowska

Zuzanna Przygodzka

Karolina Wiercińska

Warunki licencyjne do oprogramowania:
Możliwość bezpłatnego korzystania z oprogramowania bez mocy
wprowadzania zmian w kodzie źródłowym.


Architektura oprogramowania

1.	Architektura rozwoju – stos technologiczny.
   
Python, Flask, Pycharm

System kontroli wersji: GitHub

3.	Architektura uruchomieniowa – stos technologiczny.
   
Aplikacja działa na przeglądarkach: Microsoft Edge, Mozilla Firefox, Google Chrome, Safari i Opera. 








Specyfikacja wymagań

Wymagania funkcjonalne:

Identyfikator	U1

Nazwa	Uruchomienie

Opis	Każdy użytkownik może uruchomić stronę Delega w przeglądarce internetowej.

Priorytet	1


Identyfikator	RD2

Nazwa	Rodzaj delegacji

Opis	Użytkownik wybiera rodzaj delegacji – krajowa, zagraniczna lub obie.

Priorytet	1



Identyfikator	WK2
Nazwa	Wybór kraju
Opis	Użytkownik wybiera kraj, w którym odbywała się delegacja.
Priorytet	1

Identyfikator	CP2
Nazwa	Czas podróży
Opis	Użytkownik musi wskazać daty rozpoczęcia oraz zakończenia podróży dla wybranego rodzaju delegacji.
Priorytet	1

Identyfikator	ZW2
Nazwa	Zapewnione wyżywienie
Opis	Użytkownik ma możliwość wskazania ilości posiłków zapewnionych przez firmę.
Priorytet	2

Identyfikator	DKP2
Nazwa	Dodatkowe koszty podróży
Opis	Użytkownik ma możliwość wskazania liczby dni przejazdów komunikacją oraz zapewnionych noclegów.
Priorytet	2


Identyfikator	ŁCP3
Nazwa	Łączny czas podroży
Opis	Strona internetowa zlicza czas trwania delegacji (z wyszczególnieniem delegacji krajowej oraz zagranicznej)
Priorytet	1

Identyfikator	WN3
Nazwa	Wysokość należności
Opis	Strona internetowa zlicza kwotę należną za delegację.
Priorytet	1


Wymagania niefunkcjonalne:
Identyfikator	K1
Nazwa	Dostępność
Opis	Strona internetowa będzie dostępna 24h/7 365 dni w roku.
Priorytet	1

Identyfikator	K2
Nazwa	Wydajność
Opis	Przeznaczona głównie dla pracowników, biorących udział w delegacjach, natomiast będzie dostępna dla wszystkich. Nie ma ograniczeń co do
ilości osób korzystających z aplikacji w danym momencie.
Priorytet	2

Identyfikator	K3
Nazwa	Wsparcie
Opis	Zostały przeprowadzone testy manualne. Ich wyniki są pozytywne. 
Priorytet	3

Identyfikator	K4
Nazwa	Użyteczność
Opis	Strona jest intuicyjna, czytelna i nie przesycona zbędnymi
elementami, co sprawia, że jest łatwa w obsłudze.
Priorytet	2

Identyfikator	K5
Nazwa	Kompatybilność
Opis	Strona jest kompatybilna z każdym systemem operacyjnym oraz działa na wszystkich dostępnych przeglądarkach internetowych.
Priorytet	2

Testy

Identyfikator	T1
Nazwa scenariusza	Sprawdzenie kompatybilności strony internetowej
Scenariusz	Sprawdzenie kompatybilności strony internetowej z różnymi przeglądarkami.
Wynik	Pozytywny

Identyfikator	T2
Nazwa scenariusza	Sprawdzenie jakości obliczeń delegacji krajowej
Scenariusz	Formularz obliczania należnej kwoty za delegację jest poprawnie wypełniony danymi (daty, liczba noclegów, liczba dni przejazdów komunikacją, liczba posiłków). Na stronie wyświetla się informacja ile trwała podróż oraz jaka kwota należna jest użytkownikowi.
Wynik	Pozytywny

Identyfikator	T3
Nazwa scenariusza	Sprawdzenie jakości obliczeń delegacji zagranicznej
Scenariusz	Formularz obliczania należnej kwoty za delegację jest poprawnie wypełniony danymi (daty, kraj delegacji,  liczba noclegów, liczba posiłków). Na stronie wyświetla się informacja ile trwała podróż oraz jaka kwota należna jest użytkownikowi z uwzględnieniem waluty.
Wynik	Pozytywny

Identyfikator	T4
Nazwa scenariusza	Sprawdzenie jakości obliczeń delegacji łączonej
Scenariusz	Formularz obliczania należnej kwoty za delegację jest poprawnie wypełniony danymi (daty, kraj delegacji, liczba noclegów, liczba posiłków, liczba dni przejazdów komunikacją). Na stronie wyświetla się informacja ile trwała poszczególne rodzaje delegacji oraz jaka kwota należna jest użytkownikowi (w złotówkach za delegację krajową, w obowiązującej walucie za delegację zagraniczną).
Wynik	Pozytywny

