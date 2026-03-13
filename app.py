# ==============================
# Flask Framework Imports
# ==============================
from flask import Flask, request, jsonify, render_template

# ==============================
# Standard Libraries
# ==============================
import os
import logging

# ==============================
# AI Library
# ==============================
import google.genai as genai

# ==============================
# Project Modules
# ==============================
from analyzer.ai_analyzer import analyze_with_ai
from analyzer.static_analyzer import static_analysis
from analyzer.security_scanner import run_security_scan
from utils.complexity import detect_complexity


# ==============================
# App Initialization
# ==============================
app = Flask(__name__)


# ==============================
# Application Configuration
# ==============================
app.config["DEBUG"] = True
app.config["JSON_SORT_KEYS"] = False
app.config["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")
app.config["MAX_CONTENT_LENGTH"] = 1 * 1024 * 1024


# ==============================
# Logging Configuration
# ==============================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ==============================
# Routes
# ==============================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({
        "status": "running",
        "service": "AI Code Review API"
    })


# ==============================
# Code Analysis Route
# ==============================
@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.json

    code = data.get("code")
    language = data.get("language", "python")

    # Validate input
    if not code:
        return jsonify({"error": "No code provided"}), 400

    if len(code) > 5000:
        return jsonify({"error": "Code size too large"}), 400

    logging.info(f"Analysis request received for language: {language}")

    try:

        # ==============================
        # Module Orchestration
        # ==============================
        ai_result = analyze_with_ai(code)
        static_result = static_analysis(code)
        security_result = run_security_scan(code)
        complexity_result = detect_complexity(code)

        # ==============================
        # Response Generation
        # ==============================
        analysis_result = {
            "status": "success",
            "analysis": {
                "ai_analysis": ai_result,
                "static_analysis": static_result,
                "security_analysis": security_result,
                "complexity": complexity_result
            }
        }

        return jsonify(analysis_result)

    except Exception as e:

        logging.error(str(e))

        return jsonify({
            "status": "error",
            "message": "Analysis failed"
        }), 500


# ==============================
# Server Execution
# ==============================
if __name__ == "__main__":
    logging.info("Starting AI Code Review Server...")
    app.run(host="0.0.0.0", port=5000, debug=True)