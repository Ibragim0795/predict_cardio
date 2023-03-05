import streamlit as st
import pickle


st.header ("Healthy Nation")
st.write('This app is designed to help you predict the risk of cardio disease.')
st.write('Attention! Do not take the information seriously, contact your cardio doctor for more information')

def load ():
    with open ("C:/Users/Ибрагим/Desktop/app/model.pcl","rb") as fid:
        return pickle.load(fid)



id = st.slider ('id', 0,100000, key = "id")
age = st.slider('age', 29,100, key = "age")
gender = st.slider('gender', 1,2, key = "gender")
height = st.slider ('height', 120,200, key = "height")
weight = st.slider ('weight', 40,200, key = "weight")
ap_hi = st.slider ('ap_hi', 70,240, key = "ap_hi")
ap_lo = st.slider ('ap_lo', 80,150, key = "ap_lo")
cholesterol = st.slider('cholesterol',1,2,3, key = "cholesterol")
gluc = st.slider('gluc',1,3, key = "gluc")
smoke = st.slider('smoke',0,1, key = "smoke")
alco = st.slider('alco',0,1, key = "alco")
active = st.slider('active',0,1, key = "active")



model = load()
pred = model.predict_proba([[id,age,gender,height,weight,ap_hi,ap_lo,cholesterol,gluc,smoke,alco,active]])[:,1]
st.write(pred)