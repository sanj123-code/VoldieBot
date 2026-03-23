# test.py
import google.generativeai as genai

genai.configure(api_key="AIzaSyCVlXJbbgtemQn9KRaZ7-K3WGBFJ00LUpw")

model = genai.GenerativeModel(
    model_name="gemini-flash-latest",
    system_instruction="You are a strict teacher."
)

response = model.generate_content("What is the capital of India?")
print(response.text)