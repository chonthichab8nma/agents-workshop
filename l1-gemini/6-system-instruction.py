import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

system_prompt = "คุณคือแมวน้อยพันธุ์แร็กดอล ชอบร้องเหมียว ๆ"
prompt = "เหมียว เหมียว เหมียว เหมียว ขอเปียกสิบซอง"

response = client.models.generate_content(
    model='gemini-2.0-flash-lite',
    contents=prompt,
    config=types.GenerateContentConfig(
        system_instruction=system_prompt
    )
)

print(response.text)