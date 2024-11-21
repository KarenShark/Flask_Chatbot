from flask import Flask, request, jsonify
import openai

# Configure OpenAI API key
openai.api_key = "rPtlwp12ntqdsFjC1qYvhH10mYrCeqHcq2pgeUiqPdqNCddchhANf_7jcuZ0SB-2WifsrBfZA7T3BlbkFJC-eImN744_9NZac8mvAK2qbCdLkqYY1be-mjn54imN9UEhemDtaUg81xhLeCvkAY-b0PyiWMkA"

app = Flask(__name__)

@app.route("/")
def home():
    """Home route to test server status."""
    return "Welcome to the OpenAI Chatbox API!"

@app.route("/generate", methods=["POST"])
def generate():
    """Route to handle chatbox prompts."""
    data = request.json  # Get JSON body from request
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "Prompt is missing"}), 400

    try:
        # Call OpenAI's model
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can use "gpt-3.5-turbo" or "gpt-4" for newer models
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
        )
        return jsonify({"response": response["choices"][0]["text"].strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
# <<<<<<< HEAD
    app.run(host="0.0.0.0", port=5000)  # Use port 5000
# =======
    app.run(host="0.0.0.0", port=5001)  # Use port 5000
#>>>>>>> 2e73553 (Update app.py and configuration files)
