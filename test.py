# test.py
import google.generativeai as genai

genai.configure(api_key="AIzaSyDEDwX9HFKThA71B33vRWvUTSPLX_tGkRo")

model = genai.GenerativeModel(
    model_name="gemini-flash-latest",
    system_instruction="You are a strict teacher."
)

response = model.generate_content("What is the capital of India?")
print(response.text)