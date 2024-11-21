from flask import Flask, request, jsonify
import google.generativeai as genai

# Configure the Google Generative AI API Key
genai.configure(api_key="AIzaSyC1Os4Y88njQVBIdMLxYRPMZumRzcTLXoY")

app = Flask(__name__)

@app.route("/")
def home():
    """Home route to test server status."""
    return "Welcome to the LLM Chatbox API!"

@app.route("/generate", methods=["POST"])
def generate():
    """Route to handle chatbox prompts."""
    data = request.json  # Get JSON body from request
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "Prompt is missing"}), 400

    try:
        # Call Google Generative AI
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)
