import streamlit as st
import requests
import json

st.title('Delhi house rent prediction')

# Input features
bhk  = st.slider('BHK: Number of Bedrooms, Hall, Kitchen (ranges from 1 to 5)',1,5,3)
sqft = st.slider('Size: Size of the Houses/Apartments/Flats in Square Feet (ranges from 25 sqft to 4000 sqft)',25,4000,1100)
br   = st.slider('Bathroom: Number of Bathrooms (ranges from 1 to 7)',1,7,2)

# Update this URL to point to your deployed Flask API
url = 'https://flask-test-63qz.onrender.com/predict'


st.text('Predicted value:')
st.text("Rent : Rent of the Houses/Apartments/Flats")


if st.button('Predict'):
    response = requests.post(url, json={'features': [bhk,sqft,br]})
    if response.status_code == 200:
        prediction = response.json()['prediction']
        st.success(f'According to your provided input values, the rent predicted is INR : {prediction}')
    else:
        st.error('Failed to get prediction')