import streamlit as st
import requests

st.title("Echo chat!")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.chat_input("Add a message")

if user_input:
    st.session_state.history.append(("user", user_input))
    response = requests.post("http://localhost:8000/echo", json={"text": user_input})
    reply = response.json()["reply"]
    st.session_state.history.append(("bot", reply))

for role, msg in st.session_state.history:
    with st.chat_message(role):
        st.write(msg)
