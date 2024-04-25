import os  
import csv  
import pandas as pd 
from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse, JSONResponse  
from fastapi.staticfiles import StaticFiles

app = FastAPI()  # Inicjalizuje aplikację FastAPI

# app.mount("/static", StaticFiles(directory="static"), name="static")

data_file = 'gold_price_data.csv'  # Określa nazwę pliku, w którym będą przechowywane dane w formacie CSV

# @app.get('/', response_class=HTMLResponse)  # Definiuje trasę dla głównej strony
# async def index(request: Request):  # Funkcja obsługująca żądania GET na głównej stronie
#     if not os.path.exists(data_file):  # Sprawdza, czy plik danych istnieje
#         with open(data_file, 'w', newline='') as f:  # Jeśli nie istnieje, tworzy nowy plik CSV i zapisuje nagłówki kolumn
#             writer = csv.writer(f)
#             writer.writerow(['Date', 'Value'])
#     table = pd.read_csv(data_file)  # Wczytuje dane z pliku CSV do obiektu DataFrame
#     return templates.TemplateResponse("index.html", {"request": request, "table": table})  # Renderuje szablon HTML, wyświetlając tabelę danych

@app.post('/add-row')  # Definiuje trasę dla dodawania nowych wierszy do pliku CSV
async def add_row(request: Request, date: str = Form(...), price: float = Form(...)):  # Funkcja obsługująca żądania POST dodawania nowych wierszy
    new_row = {'Date': date, 'Value': price}  # Tworzy nowy wiersz danych na podstawie przesłanych danych z formularza
    with open(data_file, 'a', newline='') as f:  # Otwiera plik CSV w trybie dodawania
        writer = csv.DictWriter(f, fieldnames=['Date', 'Value'])  # Tworzy obiekt do zapisu danych do pliku CSV
        writer.writerow(new_row)  # Zapisuje nowy wiersz danych do pliku CSV
    return RedirectResponse(url='/', status_code=303)  # Przekierowuje użytkownika na główną stronę po dodaniu wiersza

@app.get("/get/data")  # Definiuje trasę dla pobierania danych
async def get_data():  # Funkcja obsługująca żądania GET pobierania danych
    dataframe = pd.read_csv(data_file)  # Wczytuje dane z pliku CSV za pomocą biblioteki Pandas
    data = dataframe.to_dict(orient='records')  # Konwertuje ramkę danych na listę słowników
    return JSONResponse(content={"data": data})  # Zwraca dane jako odpowiedź JSON
