"""
This file defines an agent that plays a "guess the number" game.

The game works as follows:
1. The agent thinks of a secret number between 0 and MAX_NUMBER.
2. The user has NUM_TURNS to guess the number.
3. After each guess, the agent tells the user if their guess was too high,
   too low, or correct.
4. The game ends if the user guesses the number correctly or runs out of turns.

Session state is used to maintain the game's status across turns. The state
is stored in `tool_context.state` and includes:
- 'secret_number': The number the user is trying to guess.
- 'turns_left': The number of remaining guesses.
- 'game_over': A boolean flag indicating if the game has concluded.
"""
import random
from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext

# Constants for the game
MAX_NUMBER = 10
NUM_TURNS = 5

def start_game(tool_context: ToolContext) -> str:
    """
    Starts a new 'guess the number' game by initializing the game state.
    This tool should be called when the user agrees to play.

    Returns:
        A description with the parameters of the game
    """
    # Check if a game is already in progress to avoid resetting it.
    if "secret_number" in tool_context.state and not tool_context.state.get("game_over", True):
        return "A game is already in progress. Keep guessing!"

    # Initialize the state for a new game
    tool_context.state["secret_number"] = random.randint(0, MAX_NUMBER)
    tool_context.state["turns_left"] = NUM_TURNS
    tool_context.state["game_over"] = False
    
    return (
        f"Great! I'm thinking of a number between 0 and {MAX_NUMBER}. "
        f"You have {NUM_TURNS} tries. What's your first guess?"
    )


def guess_number(guess: int, tool_context: ToolContext) -> str:
    """
    Processes the user's guess, compares it to the secret number,
    and tells you if the guess was too high, too low, correct, or when
    they have ran out of turns.

    Args:
        guess: The user's number guess.        

    Returns:
        A string providing feedback on the guess.
    """

    # First, check if the game has been started.
    if "secret_number" not in tool_context.state:
        return "The game hasn't started yet! Ask me to start a new game first."
        
    if tool_context.state.get("game_over", False):
        return "The game is already over. Say 'start a new game' to play again."

    secret = tool_context.state["secret_number"]
    tool_context.state["turns_left"] -= 1
    turns_left = tool_context.state["turns_left"]

    if guess == secret:
        tool_context.state["game_over"] = True        
        return "Correct!"        

    if turns_left <= 0:
        tool_context.state["game_over"] = True
        return "You ran out of turns!"

    if guess < secret:
        return "Too low."
    else:
        return "Too high."

root_agent = Agent(
    model="gemini-2.0-flash",
    name="number_guesser_agent",
    description="A friendly agent that plays a 'guess the number' game.",
    instruction="""
As a 'guess the number' game host, invite the user to play. If they agree, you
MUST call the start_game tool. For each guess, use the guess_number tool and
relay its feedback: congratulate them on a win, inform them if they're "too
high" or "too low", or reveal the if they run out of turns. 
Once game over, stop processing guesses and
ask to play again.
    """,
    tools=[start_game, guess_number],
)