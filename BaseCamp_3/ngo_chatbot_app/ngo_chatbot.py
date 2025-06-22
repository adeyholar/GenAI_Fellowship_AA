import streamlit as st
import requests
import json

st.set_page_config(page_title="NGO Chatbot", page_icon=":speech_balloon:", layout="centered")
st.title("NGO Visitor Chatbot")
st.write("Ask a question about our NGO, and get a response!")
st.write("(Hosted on Streamlit Community Cloud)")

with st.form(key="chat_form"):
    visitor_name = st.text_input("Your Name", placeholder="Enter your name")
    question = st.text_area("Your Question", placeholder="E.g., What programs does your NGO offer?")
    submit_button = st.form_submit_button("Ask")

@st.cache_data(ttl=600)
def fetch_chatbot_response(question):
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        response.raise_for_status()
        data = response.json()
        mock_response = {
            "answer": f"Thank you for your question: '{question[:50]}...'. Our NGO offers programs in education, healthcare, and community development. (Mock response from API: {data['title']})",
            "status": "success"
        }
        return mock_response
    except requests.exceptions.RequestException as e:
        return {"answer": f"Error: Could not connect to the backend ({e})", "status": "error"}

if submit_button and visitor_name and question:
    with st.spinner("Fetching response..."):
        response = fetch_chatbot_response(question)
        if response["status"] == "success":
            st.success("Response received!")
            st.write(f"**{visitor_name}**, here's our answer:")
            st.markdown(response["answer"])
        else:
            st.error(response["answer"])

        with st.expander("View Raw API Response"):
            st.json(response)

st.sidebar.header("About the Chatbot")
st.sidebar.write("This is a demo chatbot for NGO visitor engagement, hosted on Streamlit Cloud.")