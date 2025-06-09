import streamlit as st

st.title("Test Streamlit App")
st.write("Hello from Streamlit! Enter your name:")
name = st.text_input("Name")
if name:
    st.write(f"Hello, {name}! Welcome to the GenAI Fellowship!")
# This is a simple Streamlit app to test the environment setup.