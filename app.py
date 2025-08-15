from flask import Flask, request, jsonify, render_template
from assistant import analyze_screen_with_prompt
from output_audio import speak_text_to_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "Missing prompt"}), 400

    try:
        answer = analyze_screen_with_prompt(prompt)
        audio_path = speak_text_to_file(answer)
        return jsonify({
            "answer": answer,
            "audio_path": f"/{audio_path}"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)