import streamlit as st
import requests
from datetime import date
import time

# def check_model_status():
#     response = requests.get('http://model_app:5000/get_model_status/')
#     status = response.json()['status']

#     return status == 'Trained'

# with st.spinner("Waiting for FastAPI server to start..."): 
#     while not check_model_status():
#         time.sleep(4)


st.title('Przewidywanie cen złota')
st.image('./static/zloto.jpg')#
selected_data = st.date_input('Wprowadź datę', value=date(day=1, month=1, year=1971), min_value=date(day=1, month=1, year=1970), max_value= date(day=14, month = 3, year=2020))

predict_button = st.button('Wygeneruj predykcję')

if predict_button:
    response = requests.post('http://model_app:5000/predict/', json = {'date':str(selected_data)})
    
    if not response.status_code == 200:
        st.error('Nie udało się dostać predykcji')
    else:
        prediction = response.json()['prediction']
        st.success(f'Predykcja na cenę złota w {str(selected_data)} wynosi: {prediction[0][0]}')
        st.balloons()
