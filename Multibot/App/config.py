import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("My key"))

model = genai.GenerativeModel("gemini-2.0-pro")