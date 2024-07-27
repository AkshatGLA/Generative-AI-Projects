from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

# Fetch API key from environment variable
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Streamlit Page Configuration
st.set_page_config(page_title="ApnaBot", page_icon=":robot_face:")

# Streamlit Header and Subheader
st.markdown("<h1 style='text-align: center; color: #2E8B57;'>ApnaBot</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #708090;'>Chat with your creation</h4>", unsafe_allow_html=True)

# Chat History
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# User Input
input = st.text_input("You:", key="input")

submit = st.button("Send")

# Generate and display response
if submit and input:
    st.session_state['chat_history'].append(("You", input))
    response = get_gemini_response(input)
    bot_response = ""
    for chunk in response:
        bot_response += chunk.text
    st.session_state['chat_history'].append(("Gemini", bot_response))

# Display chat history
st.markdown("<div style='max-height: 400px; overflow-y: auto; padding: 10px; background-color: #f9f9f9; border-radius: 5px;'>", unsafe_allow_html=True)
for role, text in st.session_state['chat_history']:
    if role == "You":
        st.markdown(f"<div style='text-align: right; background-color: #d1e7dd; padding: 10px; border-radius: 5px; margin: 5px; color: black;'><strong>{role}:</strong> {text}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='text-align: left; background-color: #f8d7da; padding: 10px; border-radius: 5px; margin: 5px; color: black;'><strong>{role}:</strong> {text}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div style='text-align: center; color: #808080; margin-top: 20px;'>Developed with Skill Cred</div>", unsafe_allow_html=True)
