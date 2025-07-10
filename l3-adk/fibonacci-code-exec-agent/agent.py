import io
import contextlib
from google.adk.agents import Agent

# ---- ส่วนที่ 1: เราจะสร้างเครื่องมือ 'code_execution' ขึ้นมาเอง ----
# เนื่องจากเรา import โดยตรงไม่ได้ เราจึงเขียนฟังก์ชันนี้ขึ้นมาทำหน้าที่แทน
def code_execution(code: str) -> str:
    """
    Executes a string of Python code and captures its printed output.
    Args:
        code (str): The Python code to execute.
    Returns:
        str: The captured output from the print statements in the code.
    """
    # สร้าง "กล่องข้อความ" เสมือนเพื่อดักจับสิ่งที่ print ออกมา
    string_io = io.StringIO()
    try:
        # สั่งให้โปรแกรมเปลี่ยนที่ print จากหน้าจอปกติให้มาลงใน "กล่องข้อความ" ของเรา
        with contextlib.redirect_stdout(string_io):
            # รันโค้ดที่ Agent ส่งมาให้
            exec(code)
        # นำผลลัพธ์จากกล่องข้อความมาตอบกลับ
        result = string_io.getvalue()
        if not result:
            return "Code executed successfully with no output."
        return result
    except Exception as e:
        # ถ้าโค้ดที่ Agent เขียนมามีปัญหา ให้ส่ง Error กลับไป
        return f"An error occurred: {e}"

# ---- ส่วนที่ 2: เขียน Prompt ที่ชัดเจนสำหรับ Agent ----
prompt = """You are a Python programmer assistant. Your task is to solve the user's request by writing and executing a Python script.

When asked to calculate the 77th Fibonacci number, you MUST generate a complete, runnable script.
This script must define the calculation function and then print the result.

Here is the exact template you must follow:
```python
def fibonacci(n):
    a, b = 0, 1
    if n == 0:
        return a
    for _ in range(n - 1):
        a, b = b, a + b
    return b

print(fibonacci(77))

"""
root_agent = Agent(
# แก้ไขสำคัญ: เปลี่ยนไปใช้โมเดล Pro ที่เขียนโค้ดเก่งกว่า
model='gemini-1.5-pro-latest',
name='fibonacci_code_agent',
description='An agent that writes Python code to solve Fibonacci problems.',
instruction=prompt,
# ใส่เครื่องมือที่เราสร้างเองเข้าไปใน list
tools=[code_execution]
)