# Solar Industry AI Assistant

## Overview
The **Solar Industry AI Assistant** is an intelligent chatbot designed to provide expert guidance on solar energy-related topics. It helps both technical and non-technical users by answering questions about solar panel technology, installation, maintenance, cost analysis, regulations, and market trends.

## Features
- 🌞 **AI-Powered Responses**: Uses Google's Gemini API for intelligent responses.
- 🔥 **Firebase Integration**: Stores user queries and responses in Firestore.
- 🌐 **Streamlit UI**: User-friendly interface for easy interaction.
- 🚀 **Deployed on Streamlit Cloud**: Accessible online without local setup.

## Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python (FastAPI/Flask for APIs)
- **Database**: Firebase Firestore
- **AI Model**: Google Gemini API
- **Deployment**: Streamlit Cloud & Firebase

## Setup Instructions
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/iamabhishek2828/Solar-ai.git
cd Solar-ai
```

### 2️⃣ Setup Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r backend/requirements.txt
```

### 4️⃣ Configure Environment Variables
Create a `.streamlit/secrets.toml` file and add:
```toml
GEMINI_API_KEY = "your-gemini-api-key"

[firebase]
type = "service_account"
project_id = "solar-ai-assistant"
private_key_id = "your-private-key-id"
private_key = "your-private-key"
client_email = "your-firebase-client-email"
client_id = "your-firebase-client-id"
token_uri = "https://oauth2.googleapis.com/token"
```

### 5️⃣ Run the Application Locally
```sh
cd backend
streamlit run backend.py
```

## Deployment

### Live Application
[Click here to access the app](https://solar-ai-7pvz6zcgcjpmmrcbrf9ehq.streamlit.app/)

### **1. Deploying Frontend on Streamlit Cloud**
1. Push your code to GitHub.
2. Go to [Streamlit Cloud](https://share.streamlit.io/).
3. Click **New App** > Select GitHub Repo.
4. Set `backend/backend.py` as the main file.
5. Add `secrets.toml` in **App Settings**.
6. Click **Deploy**.

### **2. Deploying Backend on Firebase**
1. Enable Firestore in Firebase Console.
2. Upload your `serviceAccountKey.json`.
3. Deploy Firebase Functions if needed.

## Example Queries
- "What is the ROI of installing solar panels?"
- "How do I maintain my solar panel system?"
- "What are the latest trends in solar energy?"

## Future Improvements
- Implement user authentication.
- Enhance UI with charts and graphs.
- Add voice interaction support.

## Author
**Abhishek**

## License
MIT License


