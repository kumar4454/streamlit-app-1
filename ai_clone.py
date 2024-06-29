import streamlit as st
import google.generativeai as genai
from streamlit_option_menu import option_menu
#import speech_recognition as sr

#tite="Ai-clone-1"
#icon=":smiley:"
#st.beta_set_page_config(page_title="My Streamlit App", page_icon=":smiley:", layout="wide", initial_sidebar_state="auto")

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
                display: none;
                }
            </style>""", unsafe_allow_html=True)
            
st.markdown("""
            <style>
            .styles_terminalButton__JBj5T {
                visibility: hidden;
                display: none;
                }
            </style>""", unsafe_allow_html=True)


api=st.secrets["genai_api_key"]

genai.configure(api_key= api)
model= genai.GenerativeModel("gemini-pro")


#title

#title_html = """
#    <div style="position: fixed; top: 10px; padding: 5px 10px; border-radius: 5px;">
#        <h1>Gemini Ai Clone. </h1>
#   </div>
#"""
#st.markdown(title_html, unsafe_allow_html= True)

#st.title('My Streamlit App')
st.markdown("<h1 style='text-align:center;'>Gemini Ai Clone.</h1>", unsafe_allow_html=True) 
# sidebar...
with st.sidebar:
    b=st.sidebar.button(" :heavy_plus_sign: New Chat", help="new chat button")
    b2= st.button("speak")
    if b:
        for key in st.session_state.keys():
            del st.session_state[key]
    #if b2:
    #    transcribe_speech()
    #options
    selected=option_menu(
        menu_title=None,
        menu_icon=None,
        options=["Home","Settings","About Us"],
        icons=["house","gear wheel","book"],
        #orientation="horizontal",
    )
if "messages" not in st.session_state:
    st.session_state.messages = []


#navigation...
if selected == "Home":
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    info= st.empty()
    info.info("how can i help you today....")
    #if b2:
        #prompt=transcribe_speech()
    #prompt
    
    prompt = st.chat_input("Enter a prompt here")

    if prompt is None:
        with st.chat_message("assistant"):
            st.markdown("How can I help you today?")

    else:
        info.empty()
        with st.chat_message("user"):
            st.markdown(prompt)
        #storing prompt history
        st.session_state.messages.append({"role":"user", "content":prompt})
        #generating response
        r= model.generate_content([prompt])
        response= r.text
        #if response is created
        if response:
            with st.chat_message("assistant"):
                st.markdown(response)
            #storing response history
            st.session_state.messages.append({"role":"assistant", "content":response})
        else:
            with st.chat_message("assistant"):
                st.markdown("sorry! unable to geerate response")

elif selected == "Settings":
    st.info("settings page")

elif selected == "About Us":
    st.info("about us page")
