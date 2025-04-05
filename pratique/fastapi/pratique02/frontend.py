import streamlit as st
import requests

# URL de l'API FastAPI
API_URL = "http://127.0.0.1:8000"

st.title("Calculatrice avec Streamlit et FastAPI")

operation = st.selectbox("Choisissez une opération", ["Addition", "Soustraction", "Multiplication", "Division"])
a = st.number_input("Entrez le premier nombre", format="%f")
b = st.number_input("Entrez le deuxième nombre", format="%f")

if st.button("Calculer"):
    if operation == "Addition":
        response = requests.get(f"{API_URL}/add", params={"a": a, "b": b})
    elif operation == "Soustraction":
        response = requests.get(f"{API_URL}/subtract", params={"a": a, "b": b})
    elif operation == "Multiplication":
        response = requests.get(f"{API_URL}/multiply", params={"a": a, "b": b})
    elif operation == "Division":
        response = requests.get(f"{API_URL}/divide", params={"a": a, "b": b})
    
    if response.status_code == 200:
        result = response.json().get("result")
        st.success(f"Le résultat de {operation.lower()} est : {result}")
    else:
        st.error(f"Erreur: {response.json().get('detail')}")