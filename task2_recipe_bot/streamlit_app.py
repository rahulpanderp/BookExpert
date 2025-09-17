import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/generate"

st.title("Local Recipe Chatbot")
ingredients = st.text_input("Enter ingredients (comma-separated):")

if st.button("Get Recipe"):
    if not ingredients.strip():
        st.warning("Type some ingredients.")
    else:
        r = requests.post(API_URL, json={"ingredients": ingredients})
        if r.ok:
            data = r.json()
            st.subheader("Recipe:")
            st.write(data.get("recipe", "No recipe returned"))
        else:
            st.error(f"API error: {r.status_code} {r.text}")
