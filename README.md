# Lab2 Repo

Repozytorium zawiera program `app.py` – Serwer Flask. Serwer ten zawiera endpoint POST /classify z logiką decyzyjną przyjmującą wiek i dochód w formacie json. Następnie endpoint zwraca decyzję "Approved" lub "Rejected".

## Uruchamianie
Wymagany jest zainstalowany Docker.

1. Zbuduj obraz
```
docker build -t flask-app .
```

2. Uruchom kontener:
```
docker run -p 5000:5000 flask-app
```

## Przykładowe zapytanie POST do app.py:

```
curl -X POST http://127.0.0.1:5000/classify \
     -H "Content-Type: application/json" \
     -d '{"age": 25, "income": 4000}'
```
