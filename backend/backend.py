import streamlit as st
import google.generativeai as genai
import firebase_admin
from firebase_admin import credentials, firestore
import os

# Load Gemini API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Streamlit UI
st.title("Solar Industry AI Assistant")

query = st.text_input("Ask about solar energy:")
if st.button("Get Answer"):
    if query:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(query)
        st.write(response.text)

        # Save query & response to Firestore
        db.collection("queries").add({"query": query, "response": response.text})
    else:
        st.warning("Please enter a question!")
