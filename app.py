from dotenv import load_dotenv
load_dotenv() #loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to load gemini model
model = genai.GenerativeModel('gemini-pro')
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Streamlit app

st.set_page_config(page_title="Q&A DEMO",page_icon=":shark:")
st.header("GEMINI LLM APP",help="this is helo",divider="rainbow")
input = st.text_input("INPUT",key="input")
submit = st.button("ASk the question")


#when submit clicked

if submit:
    response = get_gemini_response(input)
    st.subheader("The response is",anchor="this is anchor")
    st.write(response)