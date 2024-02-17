from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image


import google.generativeai as genai


load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_vision_response(input, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input:
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)

    return response.text

img=r"C:\Users\vasanth rohith\OneDrive - Kau Yan College\Documents\codestuffs\geminipro\doggy.jpg"
image = Image.open(img)
# print(image)
response = get_vision_response(input="give me a description of this image", image=image)
print(response)