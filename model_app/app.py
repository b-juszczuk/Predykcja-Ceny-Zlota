from fastapi import FastAPI
import uvicorn
import pandas as pd
import requests
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense, Flatten
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    date: str  # Zmiana nazwy pola na date

# Zmiana adresu URL na aplikację danych
data_app_url = "http://data_container:7000"


# Zamiast pobierać dane bezpośrednio z aplikacji danych, będziemy teraz wysyłać zapytanie do aplikacji danych
def load_data():
    req = requests.get(f"{data_app_url}/get/data")  # Wysłanie żądania GET do aplikacji danych
    data = req.json()
    data = data["data"]

    times = [x['Date'] for x in data]
    X = [x['Value'] for x in data]

    data = np.array([(t, x) for t, x in zip(times, X)])
    
    return data

# Przygotowanie danych wejściowych i wyjściowych dla modelu LSTM
def prepare_data(data, time_steps):
    X, y = [], []
    for i in range(len(data) - time_steps):
        X.append(data[i:(i + time_steps), 1])
        y.append(data[i + time_steps, 1])
    return np.array(X), np.array(y)

# Określenie liczby kroków czasowych (w tym przypadku, możemy przyjąć 3)
time_steps = 3
# Inicjalizacja modelu LSTM
model = Sequential()
model.add(Flatten())
model.add(Dense(32, activation='relu'))
# model.add(LSTM(units=50)) # Dodanie kolejnej warstwy LSTM z 50 jednostkami
model.add(Dense(units=1)) # Dodanie warstwy gęstej z jedną jednostką wyjściową

# Kompilacja modelu
model.compile(optimizer='adam', loss='mean_squared_error')

status = 'Untrained'


# Trenowanie modelu
def train_model():
    global model
    data = load_data()  
    # data_scaled = MinMaxScaler(feature_range=(0, 1)).fit_transform(data)
    X, y = prepare_data(data, time_steps)

    train_size = int(0.75*len(X))

    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]

    X_train = X_train.astype(np.float16)
    y_train = y_train.astype(np.float16)

    X_test = X_test.astype(np.float16)
    y_test = y_test.astype(np.float16)
    
    global mms
    mms = MinMaxScaler()
    X_train = mms.fit_transform(X_train)
    X_test = mms.transform(X_test)

    global mms2
    mms2 = MinMaxScaler()
    y_train = mms2.fit_transform(y_train.reshape((-1, 1)))
    y_test = mms2.transform(y_test.reshape((-1, 1)))

    model.fit(X_train.reshape((X_train.shape[0], X_train.shape[1], 1)), y_train, epochs=30, batch_size=32, validation_split=0.2)
    status = 'Trained'



@app.post("/train")
def train():
    train_model()  # Wywołanie funkcji trenującej model
    return {"message": "Model trained successfully"}


@app.post("/predict")
async def predict(input_data: InputData):
    input_datetime = input_data.date

    # Zgromadzenie danych ze zbioru oraz wyciągniecie ostatnich obserwacji do wygenerowania predycji
    response = requests.get(f"{data_app_url}/get/data") 
    data = response.json()

    data = data['data']
    data_df = pd.DataFrame(data)
    
    pred_input = data_df.loc[data_df['Date'] < input_datetime, :].tail(n = time_steps)

    pred_input = np.array(pred_input['Value'])
    pred_input = mms.transform(pred_input.reshape(1, -1))
    
    # Wywołanie predykcji
    y_pred = model.predict(pred_input.reshape((pred_input.shape[0], pred_input.shape[1], 1)))

    y_pred = mms2.inverse_transform(y_pred.reshape((1, -1)))

    return {'prediction': y_pred.tolist()}

@app.get('/get_model_status')
async def status():
    return {'status': status}


if __name__ == "__main__":
    train_model()
    uvicorn.run(app, host="0.0.0.0", port=5000)
    