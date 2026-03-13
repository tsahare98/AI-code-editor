import requests
import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def build_prompt(code):
    return f"""
You are an expert software engineer.

Analyze the following code and provide:

1. Bugs
2. Performance issues
3. Security vulnerabilities
4. Improvements

Code:
{code}
"""


def groq(prompt):

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.1-70b-versatile",
        "messages": [{"role": "user", "content": prompt}]
    }

    r = requests.post(url, headers=headers, json=data).json()

    if "choices" in r:
        return r["choices"][0]["message"]["content"]

    raise Exception("Groq failed")


def gemini(prompt):

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

    data = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    r = requests.post(url, json=data).json()

    if "candidates" in r:
        return r["candidates"][0]["content"]["parts"][0]["text"]

    raise Exception("Gemini failed")


def openai(prompt):

    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}]
    }

    r = requests.post(url, headers=headers, json=data).json()

    if "choices" in r:
        return r["choices"][0]["message"]["content"]

    raise Exception("OpenAI failed")


def analyze_code(code):

    prompt = build_prompt(code)

    try:
        return groq(prompt)
    except:
        try:
            return gemini(prompt)
        except:
            return openai(prompt)
