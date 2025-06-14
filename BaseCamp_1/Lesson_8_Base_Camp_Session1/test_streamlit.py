import streamlit as st

st.title("My First Streamlit App")
st.write("Welcome to the Generative AI Fellowship!")
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")