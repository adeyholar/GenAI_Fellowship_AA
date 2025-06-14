import streamlit as st

st.title("Streamlit Test for GenAI Fellowship")
st.write("This is a test to verify Streamlit is working after reinstall.")
st.button("Click me to confirm!")
if st.button("Click me to confirm!"):
    st.write("Streamlit is working!")