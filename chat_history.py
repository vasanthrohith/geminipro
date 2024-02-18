from dotenv import load_dotenv
import google.generativeai as genai
import os
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel(model_name="gemini-pro")

chat = model.start_chat(history=[])



def gemini_response(question):
    response = chat.send_message(question)
    return response.text


while True:
    user = input("You : ")
    response = gemini_response(question = user)
    print("AI : ", response)
    print("Chat History >>>>", chat.history)




