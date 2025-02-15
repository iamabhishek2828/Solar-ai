import streamlit as st
import requests

st.title("Solar Industry AI Assistant 🌞")

query = st.text_input("Ask about solar energy:")
if st.button("Get Answer"):
    if query:
        response = requests.post("https://your-streamlit-cloud-backend.com", json={"query": query})
        st.write(response.json()["response"])
    else:
        st.warning("Please enter a question!")
