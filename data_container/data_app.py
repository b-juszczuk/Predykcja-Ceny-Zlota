import os  
import csv  
import pandas as pd 
from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse, JSONResponse  
from fastapi.staticfiles import StaticFiles

app = FastAPI()  # Inicjalizuje aplikację FastAPI

data_file = 'gold_price_data.csv'  # Określa nazwę pliku, w którym będą przechowywane dane w formacie CSV

@app.get("/get/data")  # Definiuje trasę dla pobierania danych
async def get_data():  # Funkcja obsługująca żądania GET pobierania danych
    dataframe = pd.read_csv(data_file)  # Wczytuje dane z pliku CSV za pomocą biblioteki Pandas
    data = dataframe.to_dict(orient='records')  # Konwertuje ramkę danych na listę słowników
    return JSONResponse(content={"data": data})  # Zwraca dane jako odpowiedź JSON
