# Interfejs aplikacji
Folder ten zawiera kod źródłowy aplikacji interfejsu użytkownika zbudowanej w środowisku Streamlit.
![apka](https://github.com/b-juszczuk/Predykcja-Ceny-Zlota/assets/115696513/95c7be10-e65f-4ee5-a7e0-9bf66c21c477)

Użytkownik wybiera datę z kalendarza a następnie po kliknięciu guzika "Wygeneruj predykcję" pojawia się przewidywana cena złota na ten dzień.

## Struktura folderu
- `static` - folder zawierający zdjęcie sztabki złota umieszczone w aplikacji,
- `Dockerfile` - plik zawierjący instrukcje służącą do zbudowania obrazu Dockera,
- `app.py`- główny skrypt aplikacji,
- `requirements.txt` - plik zawierający wszystkie paczki w kontenerze potrzebne do działania aplikacji.