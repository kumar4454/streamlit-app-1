import streamlit as st
import google.generativeai as genai
from streamlit_option_menu import option_menu

hide_st_style="""
            <style>
            #MainMenu{visibility: hidden;}
            footer{visibility: hidden;}
            header{visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
st.markdown("""
            <style>
            .viewerBadge_link__qRIco {
                visibility: hidden;
                }
            </style""", unsafe_allow_html=True)
            
st.markdown("""
            <style>
            .styles_terminalButton__JBj5T {
                visibility: hidden;
                }
            </style""", unsafe_allow_html=True)


api=st.secrets["genai_api_key"]

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

else:
    with st.chat_message("user"):
        st.markdown(prompt)
    #response= model.generate_content([prompt])
    st.session_state.messages.append({"role":"user", "content":prompt})
#else:
 #   default_prompt = "hello"
 #   response = model.generate_content([default_prompt])

    r= model.generate_content([prompt])
    response= r.text

    if response:
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role":"assistant", "content":response})
    else:
        with st.chat_message("assistant"):
            st.markdown("sorry! unable to geerate response")
