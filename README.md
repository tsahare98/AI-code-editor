# AI-code-editor
CORE_EXTRACT.AI

Neural Code Vulnerability & Efficiency Scanner

🚀 Overview

CORE_EXTRACT.AI is an intelligent code analysis tool built using Python (Flask) with an integrated AI-based evaluation system. It allows developers to scan their source code for potential vulnerabilities, inefficiencies, and complexity issues in real time.

The platform combines traditional analysis techniques with AI-driven insights to provide smarter and more meaningful feedback.

✨ Features
🔍 AI-powered code review insights
🛡️ Security vulnerability detection
⚡ Code complexity analysis
📊 Static scoring system
🌐 Web-based interface (Flask backend)
💻 Multi-language support (extensible, currently Python-focused)
🛠️ Tech Stack
Backend: Python (Flask)
Frontend: HTML, CSS, JavaScript
AI Concept:
Rule-based + AI-assisted analysis
Pattern detection for vulnerabilities
Heuristic scoring for efficiency
Deployment: Vercel (Frontend) / Flask Server

project structure

core_extract_ai/
│── __pycache__/          # Compiled Python files (auto-generated)
│
│── analyzer/             # Core AI & analysis logic
│   ├── security.py       # Security vulnerability detection
│   ├── complexity.py     # Code complexity analysis
│   ├── scoring.py        # Static scoring system
│
│── utils/                # Helper functions
│   ├── preprocess.py     # Code cleaning & preprocessing
│   ├── helpers.py        # Utility functions
│
│── templates/            # HTML templates (Frontend UI)
│   ├── index.html
│
│── static/               # CSS, JS, assets
│   ├── style.css
│   ├── script.js
│
│── app.py                # Main Flask application (entry point)
│
│── requirements.txt      # Python dependencies
│── vercel.json           # Deployment configuration (Vercel)
│── Procfile              # Deployment process file
│── .env                  # Environment variables
│── .gitignore            # Ignored files for Git
│── tempCodeRunnerFile.py # Temporary file (can be ignored)

⚙️ How It Works
User selects programming language
Pastes source code into the editor
Clicks "Execute Scan"
Backend (Flask) processes the code
AI logic analyzes:
Security risks
Code patterns
Complexity
Results are displayed:
AI Review Insight
Security Scan Status
Complexity Score
Static Score
🧑‍💻 Installation
git clone https://github.com/your-username/core-extract-ai.git
cd core-extract-ai
pip install flask
▶️ Usage

Run the Flask server:

python app.py

Then open in browser:

http://127.0.0.1:5000
🔎 Example Output

Input:
User pastes Python code

Output:

AI Review Insight: "System Ready / Suggestions"
Security Scan: "No threats detected" or flagged issues
Complexity: Calculated score
Static Score: Performance rating
🎯 Use Cases
👨‍💻 Developers: Code quality improvement
🎓 Students: Learning secure coding practices
🏢 Startups: Quick code auditing tool
🛡️ Security Enthusiasts: Basic vulnerability scanning
🔮 Future Improvements
Deep learning-based code understanding
Support for multiple languages (C++, Java, JS)
Real-time collaborative code scanning
Integration with GitHub repositories
Advanced vulnerability database (OWASP-based)
AI explanation for each detected issue
📸 Demo

(Add your deployed link or screenshots here)
Example:
👉 https://ai-code-editor-amber.vercel.app

🤝 Contributing

Contributions are welcome. Feel free to fork and submit pull requests.

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Tanmay Sahare

⭐ Vision

To build an intelligent assistant that not only detects problems in code but also teaches developers how to write better, safer, and more efficient code.
