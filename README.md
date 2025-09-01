# 🧠 Vision AI – Real-Time Visual Assistant

**Vision AI** is an intelligent screen-reading assistant that sees what’s on your screen, understands your questions, and gives you spoken answers — all in real time.

Ask questions like:
- *“What’s happening on this screen?”*
- *“How do I fix this error?”*
- *“Summarize this article for me”*

… and Vision AI will analyze the visual context and respond — **out loud and in writing**.

> 🚀 Think of it as a smart teammate always looking over your shoulder — ready to help when you’re stuck, curious, or just need a quick explanation.

---

## 🎯 What It Does

Vision AI combines **screen capture**, **multimodal AI**, and **text-to-speech** to create an assistant that:
- Captures your current screen
- Analyzes it using **Google’s Gemini Flash** (vision + language model)
- Responds to your voice or text prompts
- Speaks the answer aloud using natural-sounding audio

Perfect for:
- Accessibility tools
- Learning aids
- Debugging support
- Productivity enhancement

---

## 🛠️ Tech Stack

| Layer       | Technology |
|------------|-----------|
| Backend    | Python, Flask |
| AI Model   | Google Gemini Flash (multimodal) |
| Vision     | Screenshot capture via `mss` |
| Speech     | `gTTS` (Google Text-to-Speech), Web Speech API |
| Frontend   | HTML, CSS, Vanilla JavaScript |
| Environment| `.env` + `python-dotenv` |

---

## 🖼️ How It Works

1. **📸 Capture**: Takes a screenshot of your primary monitor
2. **🧠 Analyze**: Sends the image + your prompt to Gemini AI
3. **💬 Respond**: Gets a natural language answer
4. **🔊 Speak**: Converts the response to speech and plays it
5. **🖱️ Interface**: Clean, floating-button UI for voice input and feedback

All powered locally with a simple web interface.

---
