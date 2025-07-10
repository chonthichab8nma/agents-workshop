import os
import google.generativeai as genai

if not os.getenv("GEMINI_API_KEY"):
    print("Error: GEMINI_API_KEY not found in .env file.")
    print("Please create a .env file and add GEMINI_API_KEY='YOUR_API_KEY_HERE'")
    exit()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


recipe_text = """
Step 1:
Grind 3 garlic cloves, knob of fresh ginger, roughly chopped, 3 spring onions to a paste in a food processor.
Add 2 tbsp of clear honey, juice from one orange, 1 tbsp of light soy sauce and 2 tbsp of vegetable oil, then blend again.
Pour the mixture over the cubed chicken from 4 small breast fillets and leave to marnate for at least 1hr.
Toss in the 20 button mushrooms for the last half an hour so the take on some of the flavour, too.

Step 2:
Thread the chicken, 20 cherry tomatoes, mushrooms and 2 large red peppers onto 20 wooden skewers,
then cook on a griddle pan for 7-8 mins each side or until the chicken is thoroughly cooked and golden brown.
Turn the kebabs frequently and baste with the marinade from time to time until evenly cooked.
Arrange on a platter, and eat with your fingers.
"""

model = genai.GenerativeModel('gemini-1.5-flash-latest')

print("Running Task 1: Extracting ingredients...")

instruction_task1 = """
From the following recipe steps, extract all the ingredients and their quantities. 
List each ingredient on a new line, starting with a hyphen.
"""
prompt_task1 = f"{instruction_task1}\n\nRecipe:\n---\n{recipe_text}\n---"

response_task1 = model.generate_content(prompt_task1)

shopping_list = response_task1.text
print("\nTask 1 Complete! Here is the raw shopping list:")
print(shopping_list)


print("\n\nRunning Task 2: Categorizing the list...")

instruction_task2 = """
Organize the following shopping list into these categories: VEGETABLES, FRUIT, MEAT, SAUCES & OILS, PANTRY.
Format the output as a markdown checklist.

Here is an example of how to format the output:
---
## VEGETABLES
- [ ] 2 onions

## MEAT
- [ ] 500g ground beef

## SAUCES & OILS
- [ ] 1 tbsp olive oil
---

Now, organize this list:
"""
prompt_task2 = f"{instruction_task2}\n{shopping_list}"

response_task2 = model.generate_content(prompt_task2)

print("\nTask 2 Complete! Here is the organized shopping list:")
print(response_task2.text)