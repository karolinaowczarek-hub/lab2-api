# Lab2 Repo

Repozytorium zawiera program `app.py` – Serwer Flask. Serwer ten zawiera endpoint POST /classify z logiką decyzyjną przyjmującą wiek i dochód w formacie json. Następnie endpoint zwraca decyzję "Approved" lub "Rejected".

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
