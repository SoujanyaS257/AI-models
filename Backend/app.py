from flask import Flask, request, jsonify, send_file
from gemini_helper import process_text_prompt
from generate_2d import draw_2d_model
from generate_bim import create_ifc_model
import json

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate_model():
    try:
        data = request.json
        user_prompt = data.get("prompt")

        # Process prompt with Gemini AI
        ai_response = process_text_prompt(user_prompt)
        print("AI Response:", ai_response)

        # Convert AI output to JSON format
        structured_data = json.loads(ai_response)

        # Generate 2D Model
        draw_2d_model(ai_response)

        # Generate BIM Model
        create_ifc_model()

        return jsonify({"message": "Models Generated!", "2D_model": "2d_model.png", "BIM_model": "model.ifc"})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
