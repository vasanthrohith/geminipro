from dotenv import load_dotenv
import streamlit as st
import os
import pathlib
import textwrap

import google.generativeai as genai


# from IPython.display import display
# from IPython.display import Markdown


load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# def to_markdown(text):
#   text = text.replace('•', '  *')
#   return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))



def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

question="who is aslan in narnia"
response = get_gemini_response(question)
print(response)




