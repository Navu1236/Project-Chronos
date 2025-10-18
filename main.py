import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import google.generativeai as genai
from utils import get_contextual_sources

# Load environment variables
load_dotenv()

# Configure Gemini
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("❌ GEMINI_API_KEY missing from .env")

genai.configure(api_key=api_key)

# Flask app setup
app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/reconstruct", methods=["POST"])
def api_reconstruct():
    data = request.get_json(force=True)
    fragment = data.get("fragment", "").strip()

    if not fragment:
        return jsonify({"error": "Empty fragment provided."}), 400

    try:
        # Generate reconstruction
        model = genai.GenerativeModel("gemini-2.0-flash")
        prompt = (
            "Reconstruct the following informal or incomplete phrase into "
            "clear, natural English. Return only the corrected version.\n\n"
            f"Fragment: {fragment}"
        )

        response = model.generate_content(prompt)
        reconstructed = response.text.strip() if response.text else "No reconstruction found."

        # Fetch contextual sources (SerpAPI → Gemini fallback)
        sources = get_contextual_sources(fragment)

        return jsonify({
            "original": fragment,
            "reconstruct": reconstructed,
            "sources": sources
        })

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
