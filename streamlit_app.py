
import streamlit as st
import  pickle
st.title("🎈 My mariam VS  arwa app2")
st.header("hey , customer")
f1=st.number_input("feature 1",min_value=1,max_value=10)
f2=st.number_input("feature 2",min_value=1,max_value=10)
f3=st.number_input("feature 3",min_value=1,max_value=100)

with open('model.pkl','rb') as file:
    model=pickle.load(file)
result=model.predict([[f1,f2,f3]])
st.write("the predict value is : ")
st.write(result)
