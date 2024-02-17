from dotenv import load_dotenv
import streamlit as st
import os


import google.generativeai as genai


load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

question="who is aslan in narnia"
response = get_gemini_response(question)
print(response)




