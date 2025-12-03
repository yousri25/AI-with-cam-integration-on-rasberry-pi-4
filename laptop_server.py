from flask import Flask, request
import ollama

app = Flask(__name__)

@app.route('/ask_model', methods=['POST'])
def ask_model():
    question = request.form.get("question")
    image_file = request.files['image']
    image_bytes = image_file.read()

    # Generate response using local LLaVA model
    try:
        response = ollama.generate(
            model="llava:7b",  # replace if needed
            prompt=question,
            images=[image_bytes]
        )
        return response.get("response", "No response")
    except Exception as e:
        return f"Error generating response: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
