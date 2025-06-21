import streamlit as st
import requests

# Streamlit App
st.title("Calculator App")
st.write("Interact with the Calculator API built using FastAPI")

# Input Fields
operation = st.selectbox("Select Operation", ["add", "subtract", "multiply", "divide"])
num1 = st.number_input("Enter First Number", value=0.0)
num2 = st.number_input("Enter Second Number", value=0.0)

if st.button("Calculate"):
    try:
        # Make API Request
        response = requests.post(
            "http://127.0.0.1:8000/calculate",
            json={"operation": operation, "num1": num1, "num2": num2}
        )
        response.raise_for_status()
        result = response.json()
        st.success(f"Result: {result['num1']} {operation} {result['num2']} = {result['result']}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {str(e)}")