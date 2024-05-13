## Punkty końcowe
- **/get/data** - GET API do pobierania danych z pliku gold_price_data.csv.

Kontener ten odpowiada za pobranie danych z pliku .csv i wysłaniu ich to kontenera **model_app** w celu trenowania modelu.
przedstawiony kontener jest mapowany na porcie `http://localhost:7000/docs`.


## Struktura folderu:
- `Dockerfile`- plik zawierjący instrukcje służącą do zbudowania obrazu Dockera,
- `data_app.py`- plik skrytpu FastAPI.
- `gold_price_data.csv`- plik zawierający dane do uczenia modelu,
- `requirements.txt`-plik zawierający wszystkie paczki w kontenerze potrzebne do działania aplikacji.
