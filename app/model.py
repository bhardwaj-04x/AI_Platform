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
