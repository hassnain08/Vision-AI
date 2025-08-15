# audio_output.py
from gtts import gTTS
import uuid
import os

def speak_text_to_file(text, lang="en"):
    try:
        print("🗣️ Generating voice...")
        # Save file in the Flask static folder
        filename = f"static/response_{uuid.uuid4().hex}.mp3"
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save(filename)

        print(f"✅ Audio saved at: {filename}")
        return filename  # Return path to frontend
    except Exception as e:
        print("❌ Error in TTS:", e)
        return None