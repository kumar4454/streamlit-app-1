import streamlit as st
import google.generativeai as genai
from streamlit_option_menu import option_menu
#api=st.secrets["genai_api_key"]
api="AIzaSyDokwegR04F-D94Olo8l8QcgVpd6MCJ0QU"
genai.configure(api_key= api)
model= genai.GenerativeModel("gemini-pro")

#title

st.markdown("<h1 style='text-align:center'>Gemini Ai Clone.</h1>", unsafe_allow_html=True) 

if "messages" not in st.session_state:
    st.session_state.messages = []

selected=option_menu(
    menu_title=None,
    menu_icon=None,
    options=["home","settings","about us"],
    icons=["house","gear wheel","book"],
    orientation="horizontal",
)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#prompt
prompt = st.chat_input("enter your prompt")

if prompt is None:
    with st.chat_message("assistant"):
        st.markdown("hello, how can i help you")
#else:
#    print("Error: Input data 'p' is None.")


if prompt is not None:
    with st.chat_message("user"):
        st.markdown(prompt)
    #response= model.generate_content([prompt])
    st.session_state.messages.append({"role":"user", "content":prompt})
#else:
 #   default_prompt = "hello"
 #   response = model.generate_content([default_prompt])

response= model.generate_content([prompt])

if response:
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role":"assistant", "content":response.text})
