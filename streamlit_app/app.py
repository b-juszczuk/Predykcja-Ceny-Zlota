import streamlit as st
import requests
from datetime import date
import time


st.title('Przewidywanie cen złota')
st.image('./static/gold.jpg', width=200)
selected_data = st.date_input('Wprowadź datę', value=date(day=1, month=1, year=2015), min_value=date(day=1, month=1, year=1979), max_value= date(day=14, month = 3, year=2020))

predict_button = st.button('Wygeneruj predykcję')

if predict_button:
    response = requests.post('http://model_app:5000/predict/', json = {'date':str(selected_data)})
    
    if not response.status_code == 200:
        st.error('Nie udało się dostać predykcji')
    else:
        prediction = response.json()['prediction']
        st.success(f'Predykcja na cenę złota w {str(selected_data)} wynosi: {prediction[0][0]}')
        st.balloons()
