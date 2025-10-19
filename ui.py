import streamlit as st
import requests
st.set_page_config(page_title="Data Redundancy UI")
st.title("Data Redundancy Removal System - UI (Local)")

st.write("Fill fields and submit. Backend must be running at http://127.0.0.1:5000")

name = st.text_input("Name")
email = st.text_input("Email")
age = st.number_input("Age", min_value=0, step=1)

if st.button("Submit"):
    payload = {"name": name, "email": email, "age": age}
    try:
        r = requests.post("http://127.0.0.1:5000/add", json=payload, timeout=5)
        st.write("Status code:", r.status_code)
        st.json(r.json())
    except Exception as e:
        st.error("Failed to contact backend: " + str(e))

if st.button("Show all stored"):
    try:
        r = requests.get("http://127.0.0.1:5000/all", timeout=5)
        st.write("Status code:", r.status_code)
        st.json(r.json())
    except Exception as e:
        st.error("Failed to contact backend: " + str(e))
