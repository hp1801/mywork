# Simple FAQ Assistant

A basic FAQ assistant built with Streamlit and Flask.

## Setup Instructions

1. Install required packages:
```bash
pip install streamlit flask flask-cors requests
```

2. Save these files in your project folder:
   - `faq_frontend.py` (Streamlit frontend)
   - `faq_backend.py` (Flask backend)
   - `faq.json` (FAQ data)

3. Run the application:
   - Start the backend server:
     ```bash
     python faq_backend.py
     ```
   - In a new terminal, start the Streamlit app:
     ```bash
     streamlit run faq_frontend.py
     ```

4. Open your web browser and go to the URL shown in the Streamlit output (usually http://localhost:8501)

## How to Use

1. Type your question in the text box
2. Click "Get Answer"
3. The answer will appear below

## Features

- Simple search interface
- Basic error handling
- Loading states
- JSON-based FAQ storage