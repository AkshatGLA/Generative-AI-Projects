from dotenv import load_dotenv
load_dotenv()  # Loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("AIzaSyAj_0k-ytzFBaw6JDW7ZyU4cABbyMV6EfA"))


# function to load gemini model and get response
model=genai.GenerativeModel('gemini-1.5-flash')
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

if submit:
    response=get_gemini_response(input)
    st.write(response)