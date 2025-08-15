# assistant.py
import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("❌ GOOGLE_API_KEY not found in .env file.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

# Load static image paths (update these paths!)
IMAGE_1_PATH = "static/graph1.png"
IMAGE_2_PATH = "static/graph2.png"

def analyze_screen_with_prompt(prompt: str) -> str:
    try:
        image1 = Image.open(IMAGE_1_PATH)
        image2 = Image.open(IMAGE_2_PATH)

        print("⏳ Sending to Gemini...")
        response = model.generate_content([prompt, image1, image2])
        return response.text.strip()

    except Exception as e:
        print(f"❌ Gemini error: {e}")
        return "Failed to analyze images."