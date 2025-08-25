# assistant.py
import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
from screen_capture import capture_screenshot

# Load API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("❌ GOOGLE_API_KEY not found in .env file.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

def analyze_screen_with_prompt(prompt: str) -> str:
    try:
        # 1. Capture screenshot
        screenshot_path = "live_screen.png"
        capture_screenshot(screenshot_path)

        # 2. Load image
        image = Image.open(screenshot_path)

        # 3. Send to Gemini
        print("⏳ Sending to Gemini with screenshot...")
        response = model.generate_content([prompt, image])

        # 4. Return text response
        return response.text.strip()

    except Exception as e:
        print(f"❌ Gemini error: {e}")
        return "Failed to analyze screenshot with prompt."
