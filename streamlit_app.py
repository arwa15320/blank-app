import streamlit as st
import pickle

# Set up the page title and layout
st.set_page_config(page_title="🎈 My Mariam VS Arwa App", page_icon="🎈", layout="centered")

# Custom CSS to improve UI design
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        color: white;
        background-color: #4CAF50;
    }
    .stSlider > div > div > div > div > div {
        background: linear-gradient(90deg, rgba(255,0,150,1) 0%, rgba(0,204,255,1) 100%);
    }
    .stSelectbox>div>div>div {
        background-color: #FFFFFF;
    }
    </style>
    """, unsafe_allow_html=True)

# App title and header with emoji
st.title("🎈 My Mariam VS Arwa App")
st.header("Welcome, Customer!")

# Display an image (replace 'your_image.png' with the path to your image)
st.image("your_image.png", caption="Predictive Analysis", use_column_width=True)

# Create user-friendly input fields with sliders, dropdowns, and other controls
st.subheader("Please enter the features below:")

# Use sliders for feature inputs
f1 = st.slider("Select Feature 1", min_value=1, max_value=10, value=5)
f2 = st.slider("Select Feature 2", min_value=1, max_value=10, value=5)
f3 = st.slider("Select Feature 3", min_value=1, max_value=100, value=50)

# Additional inputs for more user options
user_name = st.text_input("Enter your name")
feature_select = st.selectbox("Select an additional feature", options=["Feature A", "Feature B", "Feature C"])
preference = st.radio("Choose your preference", options=["Option 1", "Option 2", "Option 3"])
confirm = st.checkbox("I confirm that the above information is correct")

# Button to trigger prediction
if st.button("Predict"):
    if confirm:
        with open('model.pkl', 'rb') as file:
            model = pickle.load(file)
        
        # Perform prediction
        result = model.predict([[f1, f2, f3]])
        
        # Display the result
        st.success(f"Hello {user_name}, the predicted value is: {result[0]}")
    else:
        st.error("Please confirm that the information is correct.")
else:
    st.info("Please adjust the sliders and click 'Predict' to see the result.")
