# Aplikacja do przewidywania ceny złota
To repozytorium zawiera aplikację z funkcją uczenia, która przewiduję cenę złota w okresie od 01.01.1979 do 14.03.2020. 
Do zarządzania kontenerami wykorzystano aplikację Docker.

![zloto](https://github.com/b-juszczuk/Predykcja-Ceny-Zlota/assets/115696513/bccfc535-4be9-4abc-8a47-e50bc5fc4635)

**Struktura projektu:** 

```markdown
Predykcja_Ceny_Zlota
│   ├── data_container
│   │   ├── Dockerfile
│   │   ├── data_app.py
|   |   ├── gold_price_data.csv
|   |   ├── README.md
│   │   └── requirements.txt
│   ├── model_app
│   │   ├── app.py
│   │   ├── Dockerfile
|   |   ├── README.md
│   │   └── requirements.txt
│   ├── streamlit_app
|   |   ├── static/gold.jpg
|   |   ├── app.py
|   |   ├── Dockerfile
|   |   ├── README.md
│   │   └── requirements.txt
│   ├── docker-compose.yml
│   └── README.md
```

- `data_container`- kontener odpowiadający za przesłanie danych do uczenia, 
- `model_app`- kontener odpowiadający za uczenie modelu,
- `streamlit_app` - kontener odpowiadający za wygląd interfejsu użytkownika,
- `docker-compose.yml` - skrypt odpowiadający za kontaktowanie pomiędzy kontenerami,
- `README.md` - plik zawierający instrukcję.

# Jak uruchomić
Aby uruchomic aplikacje na początku sklonuj to repozytorium.

```markdown
git clone https://github.com/b-juszczuk/Predykcja-Ceny-Zlota.git
```
Następnie przejdź do katalogu aplikacji. Używając poniższej komendy zbuduj i uruchom aplikację.
```markdown
docker-compose up --build
```
Otwórz przeglądarkę internetową i przejdź do http://localhost:80, aby przetestować aplikację.

> :warning: **Ostrzeżenie:**
>
> Jeśli pojawi się błąd po naciśnięciu przycisku "Wygeneruj predykcję" odczekaj chwilę iponownie naciśnij przycisk, prawdopodobnie trwa uczenie modelu i dlatego pojawia sie błąd.

