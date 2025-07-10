import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

system_prompt = """
สวัสดี! คุณคือแชทบอท AI สำหรับเว็บไซต์ท่องเที่ยว
ภารกิจของคุณคือการให้ข้อมูลและคำแนะนำที่เป็นประโยชน์แก่นักเดินทาง
โปรดจำไว้ว่า ก่อนที่คุณจะตอบคำถามใดๆ คุณต้องตรวจสอบว่าคำถามนั้นสอดคล้องกับภารกิจของคุณหรือไม่
หากไม่เป็นเช่นนั้น คุณสามารถตอบได้ว่า "ขออภัย ฉันไม่สามารถตอบคำถามนั้นได้"
"""
prompt = "แนะนำสถานที่ท่องเที่ยวในภูเก็ตหน่อย"

response = client.models.generate_content(
    model='gemini-2.0-flash-lite',
    contents=prompt,
    config=types.GenerateContentConfig(
        system_instruction=system_prompt
    )
)

print("\nResponse:")
print(response.text)