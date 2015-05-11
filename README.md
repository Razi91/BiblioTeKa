#BiblioTeKa

System zarządzania biblioteką

#Wymagania

*Python 3.3
*Django 1.8
*PostgreSQL (lub inna baza danych, SQLite odradzany)


#Uruchomienie aplikacji

1. Zaopatrz się w wymagane oprogramowanie (wyżej wymienione)
2. Uruchom kolejno:
  2.1 `python3 manage.py syncdb` -- utworzenie schematu bazy danych, tworzy też konto superadmina
  2.2 `python3 manage.py migrate` -- (nie wiem czy wymagane, nie chce mi się zagłębiać)
  2.3 `python3 manage.py randoms` -- utworzenie losowej bazy danych
3. Uruchom serwer:
`python manage.py runserver 0.0.0.0:8000`

Po tym serwer stoi na twoim lokalnym komputerze na porcie 8000 i jest dostępny dla wszystkich klientów z dostępem do tego portu

Jeżeli używasz innej bazy danych, skopiuj plik btk/settings.py, zmień ustawienia dostępu do bazy danych, a przy każdej
komendzie dopisuj ` --settings=plik.z.ustawieniami` (pamiętaj że to nazwa paczki, więc kropni, a nie slashe). Nie używaj spacji