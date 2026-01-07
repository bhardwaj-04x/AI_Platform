# This is the paid API Calling code using OpenAI's Python SDK.

# from openai import OpenAI
# import os

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def chatbot_response(user_text):
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "user", "content": user_text}
#         ]
#     )
#     return response.choices[0].message.content
import subprocess

def chatbot_response(user_text):
    try:
        result = subprocess.run(
            ["ollama", "run", "mistral", user_text],
            capture_output=True,
            text=True,
            encoding="utf-8",   # <--- force UTF-8
            errors="ignore"     # <--- ignore un-decodable characters
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {str(e)}"
