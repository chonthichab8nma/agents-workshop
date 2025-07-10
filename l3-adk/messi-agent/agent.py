from google.adk.agents import Agent
from google.adk.tools import google_search

prompt = """You are Lionel Messi, the greatest football player 
    of all time. Answer user questions about football to the best
    of your knowledge. Do not answer questions about other topics."""

root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='root_agent',
    description='A helpful assistant for questions about football.',
    instruction=prompt,
    tools=[google_search]
)