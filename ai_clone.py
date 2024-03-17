import streamlit as st
import google.generativeai as genai
genai.configure(api_key="AIzaSyDokwegR04F-D94Olo8l8QcgVpd6MCJ0QU")
model= genai.GenerativeModel("gemini-pro")

#title

st.markdown("<h1 style='text-align:center'>Gemini Ai Clone.</h1>", unsafe_allow_html=True) 

d="<div style='border:solid black 2px'>hello</div>"
st.markdown(d, unsafe_allow_html=True)

#prompt
#h=[]
p=st.text_input(label="", placeholder="enter a prompt here.")
clicked=st.button("ask....")
c=st.button("history")
if clicked:
    #h.append(p)
    #st.write(h)
    st.write(f"prompt you entered:  {p}")
    response= model.generate_content([p])
    st.write(response.text)
    st.write("thank you...!!")
#if c:
    #st.write(f"history: {h}")
