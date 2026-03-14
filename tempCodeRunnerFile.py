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