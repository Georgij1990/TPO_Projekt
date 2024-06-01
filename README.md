Georgij Kocsarjan s24171

Kalkulator.

Aplikacja umożliwia wykonywanie ciągu działań arytmetycznych. Wynik każdego działania może być użyty jako operand w następnym działaniu.

Aplikacja obsługuje następujące operacje matematyczne: Dodawanie (+) Odejmowanie (-) Mnożenie (*) Dzielenie (/) Potęgowanie (^) Pierwiastkowanie (sqrt) Procenty (%) Silnia (!) Operacje trygonometryczne (sin, cos, tan, cot)

Aplikacja automatycznie wyświetla historię ostatnich pięciu operacji. Użytkownik może przeglądać historię za pomocą strzałek góra/dół.

Aplikacja 'Kalkulator' składa się z czterech głównych klas, z których każda odpowiada za różne aspekty funkcjonalności kalkulatora konsolowego:

Klasa Operations.
Funkcjonalność: Klasa ta definiuje wszystkie podstawowe operacje matematyczne, takie jak dodawanie, odejmowanie, mnożenie, dzielenie, potęgowanie, pierwiastkowanie, operacje trygonometryczne (sin, cos, tg, ctg) oraz inne zaawansowane operacje jak silnia czy procenty. 
Cel: Dostarczenie metod, które będą wykorzystywane przez inne klasy do wykonywania rzeczywistych obliczeń matematycznych.

Klasa Utils.
Funkcjonalność: Klasa ta zawiera metody do obsługi wyrażeń matematycznych w postaci tekstowej. Obejmuje metody wywołujące operacje matematyczne zdefiniowane w klasie Operations. 
Dodatkowe Funkcje: Ewaluacja Wyrażeń: Przetwarza wyrażenia matematyczne, konwertując je z formatu tekstowego do postaci, która może być obliczona. Obsługa Transakcji: Metody do zarządzania historią transakcji, takie jak dodawanie nowych transakcji do historii.

Klasa Calculate.
Funkcjonalność: Zarządza operacjami matematycznymi w aplikacji konsolowej kalkulatora. 
Główne Zadania: Przechowywanie Wyniku: Przechowuje wynik ostatniego działania, umożliwiając wykorzystanie go w kolejnych obliczeniach. 
Historia Transakcji: Przechowuje historię wszystkich wykonanych operacji. Obsługa Błędów: Zajmuje się obsługą błędów, takich jak podanie nieprawidłowego znaku, dzielenie przez zero czy wpisanie błędnego polecenia.

Klasa Calculator.
Funkcjonalność: Przedstawia główną funkcjonalność aplikacji kalkulatora, integrując wszystkie funkcje z klas Operations, Utils i Calculate. 
Główne Zadania: 
Interfejs Użytkownika: Zapewnia interaktywny interfejs konsolowy, w którym użytkownik może wprowadzać wyrażenia matematyczne. 
Obsługa Wyrażeń: Umożliwia użytkownikowi wykonywanie działań matematycznych, korzystając z metod z innych klas. 
Historia i Nawigacja: Obsługuje wyświetlanie i nawigację po historii transakcji za pomocą klawiatury (strzałki góra/dół). 


Podsumowanie.
Aplikacja 'Kalkulator' jest zorganizowana w sposób modułowy, gdzie każda klasa ma jasno zdefiniowane odpowiedzialności. 
Klasa Operations dostarcza podstawowych operacji matematycznych, Utils obsługuje i przetwarza wyrażenia, Calculate zarządza wynikami i historią, a Calculator integruje wszystkie te funkcje, oferując użytkownikowi interaktywny interfejs konsolowy.
