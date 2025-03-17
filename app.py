import streamlit as st
import requests
import json

# Konfigurasi API OpenRouter
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"]  # Ganti dengan API key Anda
HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

# Fungsi untuk menghasilkan respons dari AI
def generate_response(prompt):
    data = {
        "model": "google/gemma-3-12b-it:free",  # Model Gemma3
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        response = requests.post(OPENROUTER_API_URL, headers=HEADERS, json=data)
        response.raise_for_status()  # Cek jika ada error dalam respons
        result = response.json()
        return result['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Antarmuka Streamlit
st.title("QNA dengan AI (Gemma3)")

# Input dari pengguna
user_input = st.text_input("Masukkan pertanyaan Anda:")

# Tombol untuk mengirim pertanyaan
if st.button("Kirim"):
    if user_input:
        with st.spinner("Menunggu respons..."):  # Tampilkan spinner saat menunggu
            ai_response = generate_response(user_input)
        st.success("Respons dari AI:")
        st.write(ai_response)
    else:
        st.warning("Silakan masukkan pertanyaan terlebih dahulu.")
