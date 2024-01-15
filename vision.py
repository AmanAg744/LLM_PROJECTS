from dotenv import load_dotenv
load_dotenv() #loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to load gemini model
model = genai.GenerativeModel('gemini-pro-vision')
def get_gemini_response(input,image):
    if input is not None:
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)

    return response.text

#initalize the streamlit app

st.set_page_config(page_title="GEMINI PRO VISION",page_icon=":camera:")
st.header("Gemini Application Image")
input  = st.text_input("Input Prompt", key="input")

#file upload

uploaded_file = st.file_uploader("Choose an image.....",type=["jpeg","jpg","png","webp"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="uploaded image")


submit = st.button("tell me about the image")

if submit:
    response = get_gemini_response(input,image)
    st.subheader("the response is --")
    st.write(response)