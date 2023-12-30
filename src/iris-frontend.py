import streamlit as st
import requests


st.image('assets/header-iris.png', caption='Iris Flower')
st.title('Iris Flower Classification')
st.markdown('Created by: Farrel Arrizal | Batch Period: SEP 2023 | HAPPY NEW YEAR')

st.divider()

st.subheader('Just type the value, then click the button to predict the flower type :sunglasses:')

# Form Input
with st.form("iris-form"):
    sepal_length = st.number_input('Sepal Length', min_value=0.0,  step=0.1, help='Centimeter')
    sepal_width = st.number_input('Sepal Width', min_value=0.0,  step=0.1, help='Centimeter')
    petal_length = st.number_input('Petal Length', min_value=0.0,  step=0.1, help='Centimeter')
    petal_width = st.number_input('Petal Width', min_value=0.0,  step=0.1)
    
    submit_button = st.form_submit_button(label='Predict')
    
    if submit_button:
        data = {
            'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width
        }
        
        with st.spinner('Predicting...'):
            
            # Send request to backend
            response = requests.post('http://backend:8000/predict', json=data)
            result = response.json()
            
            # if success
            if result['status'] == 200:
                st.success(f"Prediction Success, Your Iris Flower is **{result['prediction']}** ")
                st.balloons()
                
            else:
                st.error('Prediction Failed')
        
    
    