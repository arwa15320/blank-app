import streamlit as st
import pickle

# Set up the page title and header
st.set_page_config(page_title="🎈 My Mariam VS Arwa App", page_icon="🎈", layout="centered")
st.title("🎈 My Mariam VS Arwa App")
st.header("Welcome, Customer!")
# Input features
st.subheader("Please enter the features below:")
f1 = st.number_input("Feature 1", min_value=1, max_value=10)
f2 = st.number_input("Feature 2", min_value=1, max_value=10)
f3 = st.number_input("Feature 3", min_value=1, max_value=100)

# Button to trigger the prediction
if st.button("Predict"):
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    
    # Perform prediction
    result = model.predict([[f1, f2, f3]])
    
    # Display the result
    st.write("The predicted value is:")
    st.write(result)
else:
    st.write("Please input all features and press 'Predict' to see the result.")
