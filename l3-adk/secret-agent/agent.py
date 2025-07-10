from google.adk.agents import Agent

def verify_secret_passcode(secret: str) -> bool:
    """Given a secret passcode, verify if it matches the expected value."""
    return secret == '1984'

root_agent = Agent(
    model='gemini-2.0-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    tools=[verify_secret_passcode]
)