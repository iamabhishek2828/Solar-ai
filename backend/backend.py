import streamlit as st
import google.generativeai as genai
import firebase_admin
from firebase_admin import credentials, firestore
import json

# Load Gemini API Key
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)

# Load Firebase Credentials
firebase_creds = json.loads(st.secrets["FIREBASE_CREDENTIALS"])

# Fix private key formatting (convert \\n to actual newlines)
firebase_creds["private_key"] = firebase_creds["private_key"].replace('\\n', '\n')

# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_creds)
    firebase_admin.initialize_app(cred)

# Firestore Database
db = firestore.client()

