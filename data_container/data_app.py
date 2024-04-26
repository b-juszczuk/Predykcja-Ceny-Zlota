import os  
import csv  
import pandas as pd 
from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse, JSONResponse  
from fastapi.staticfiles import StaticFiles

app = FastAPI()  # Inicjalizuje aplikację FastAPI

data_file = 'gold_price_data.csv'  # Określa nazwę pliku, w którym będą przechowywane dane w formacie CSV

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
