import streamlit as st
import google.generativeai as genai
import firebase_admin
from firebase_admin import credentials, firestore
import json

# Load Gemini API Key
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)

# Convert Firebase Credentials (Ensure it's a dict)
firebase_creds = json.loads(json.dumps(st.secrets["FIREBASE_CREDENTIALS"]))

# Fix private key formatting (replace escaped newlines)
firebase_creds["private_key"] = firebase_creds["private_key"].replace('\\n', '\n')

# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_creds)
    firebase_admin.initialize_app(cred)

# Firestore Database
db = firestore.client()

# Streamlit UI
st.title("🌞 Solar Industry AI Assistant")

query = st.text_input("🔍 Ask about solar energy:")
if st.button("Get Answer"):
    if query:
        try:
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(query)

            # Display response
            st.write("💡 **AI Response:**")
            st.write(response.text)

            # Save query & response to Firestore
            db.collection("queries").add({"query": query, "response": response.text})

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("⚠️ Please enter a question!")

