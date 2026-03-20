import sys
import streamlit as st
import requests

def is_streamlit():
    return "streamlit" in sys.modules

st.title("Multi Agent System")

query = st.text_input("Enter your query:")

if st.button("Send"):
    response = requests.get(f"http://localhost:8000/chat?query={query}")
    st.write(response.json()["response"])