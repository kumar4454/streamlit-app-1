import streamlit as st
import google.generativeai as genai
from streamlit_option_menu import option_menu

api=st.secrets["genai_api_key"]

genai.configure(api_key= api)
model= genai.GenerativeModel("gemini-pro")

#title

st.markdown("<h1 style='text-align:center'>Gemini Ai Clone.</h1>", unsafe_allow_html=True) 

with st.sidebar:(
    st.button("New Chat"),
    st.write("clicked")
)

selected=option_menu(
    menu_title=None,
    menu_icon=None,
    options=["home","settings","about us"],
    icons=["house","gear wheel","book"],
    orientation="horizontal",
)

#prompt
p=st.chat_input("enter your prompt")

if p is None:
    # Handle the case where p is None
    p = ""

if p:
    with st.chat_message("user"):
        st.markdown(p)

response= model.generate_content([p])
if response:
    with st.chat_message("assistant"):
        st.markdown(response.text)
