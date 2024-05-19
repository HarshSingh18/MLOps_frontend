import streamlit as st
import requests
import json

<<<<<<< HEAD
st.set_page_config(
    page_title="Delhi House Rent Prediction",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.title('🏠 Delhi House Rent Prediction')
st.write("""
Welcome to the Delhi House Rent Prediction app.""")
         
=======

st.set_page_config(page_title="MLops Project")
st.title('Delhi house rent prediction')

st.text("This application is used to predict house rent prediction for the city of Delhi")

>>>>>>> 9ee7184279fe9979c4ece1dae8ee4e1309023c70
# Input features
bhk  = st.slider('BHK: Number of Bedrooms, Hall, Kitchen',1,5,3)
sqft = st.slider('Size: Size of the Houses/Apartments/Flats in Square Feet',25,4000,1100)
br   = st.slider('Bathroom: Number of Bathrooms',1,7,2)



# Update this URL to point to your deployed Flask API
url = 'https://flask-test-63qz.onrender.com/predict'
st.text("Feature to predict : Rent of the Houses/Apartments/Flats")
if st.button('Predict'):
    response = requests.post(url, json={'features': [bhk,sqft,br]})
    if response.status_code == 200:
        prediction = response.json()['prediction']
        st.success(f'According to your provided input values, the rent predicted is INR : {prediction}')
    else:
        st.error('Failed to get prediction')

<<<<<<< HEAD
st.markdown("""
---
Developed by [Anupam Dhiman, Harsh Singh & Lokesh Arora](https://github.com/lokesharoraa).
""")
=======
st.text_area(
    "Created By -"
    "Anupam Dhiman"
    "Harsh Singh"
    "Lokesh Arora")
>>>>>>> 9ee7184279fe9979c4ece1dae8ee4e1309023c70
