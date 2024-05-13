## Trenowanie modelu

Kontener ten odpowiada za pobranie plików z kontenera **data_container**, 
przekonwenterowanie tych danych, a następnie na ich podstawie dokonuje się
treningu modelu. Nastęonie dla wybranej daty zwraca przewidywaną cenę złota.

Kontener ten jest mapowany na porcie `http://localhost:5000/docs`

## Punkty końcowe
- **/post/train** - trenowanie modelu
- **/post/predict** - zwraca przewidywaną cenę złota dla wybranej daty

![image](https://github.com/b-juszczuk/Predykcja-Ceny-Zlota/assets/115696513/4c72423e-7b64-4c1f-aaf4-37b9e2c7290c)
![image](https://github.com/b-juszczuk/Predykcja-Ceny-Zlota/assets/115696513/03b57c98-7684-4494-b064-cf777aa7ee69)

## Struktura folderu:
- `app.py`- plik zawierający głowny skrypt aplikacji,
- `Dockerfile`- plik zawierjący instrukcje służącą do zbudowania obrazu Dockera,
- `requirements.txt`- plik zawierający wszystkie paczki w kontenerze potrzebne do działania aplikacji.
