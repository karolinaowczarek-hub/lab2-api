# Lab2 Repo

Repozytorium zawiera cztery programy:

1. `program1.py` – Pobiera dane z API i wypisuje odpowiedź.
2. `program2.py` – Zapisuje odpowiedź z API do pliku.
3. `program3.py` – Serwer Flask z prostym endpointem `/hello`.
4. `app.py` – Serwer Flask z logiką decyzyjną przyjmującą wiek i dochód.

## Uruchamianie

1. Zainstaluj wymagania:
```
pip install -r requirements.txt
```

2. Uruchom aplikację:
```
python app.py
```

## Przykładowe zapytanie POST do app.py:

```
curl -X POST http://127.0.0.1:5000/classify \
     -H "Content-Type: application/json" \
     -d '{"age": 25, "income": 4000}'
```