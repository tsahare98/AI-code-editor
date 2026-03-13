import os
from google import genai

# Initialize Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_with_ai(code):

    prompt = f"""
You are an expert software engineer.

Analyze the following code and provide:

1. Bugs or syntax issues
2. Performance problems
3. Security vulnerabilities
4. Suggested improvements

Code:
{code}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"AI analysis error: {str(e)}"