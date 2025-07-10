from google.adk.agents import Agent

def fibonacci_tool(n: int) -> str:
    """
    Calculates the n-th Fibonacci number and returns it as a formatted string.
    The sequence starts with F(0)=0 and F(1)=1.
    """
    if not isinstance(n, int) or n < 0:
        raise TypeError("Input must be a non-negative integer.")
        
    a, b = 0, 1
    if n == 0:
        number = a
    else:
        for _ in range(n - 1):
            a, b = b, a + b
        number = b

    return f"The {n}th number in the Fibonacci sequence is {number:,}."

prompt = """You are a mathematical assistant. When a user asks for a Fibonacci number, 
you MUST use the `fibonacci_tool` to find the answer.
You MUST respond with the exact text provided by the tool's output."""

root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='fibonacci_agent',       
    description='An agent that can accurately calculate Fibonacci numbers using a tool.',
    instruction=prompt,
    tools=[fibonacci_tool]  
)