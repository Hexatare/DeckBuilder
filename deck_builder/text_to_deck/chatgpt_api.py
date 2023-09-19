"""
This module takes in a factual text and returns either a deck of flashcards or raises an error.
"""


# Imports
import ast
from os import environ, path
from dotenv import load_dotenv
import openai

# Load the .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))
openai.api_key = environ.get("OPENAIAPIKEY")

# Use GPT-3.5 Turbo for now, maybe switch to GPT-4?
MODEL_ENGINE = "gpt-3.5-turbo"


def prompt_chatgpt(factual_text: str) -> tuple[bool, list[tuple] | str]:
    """
    This function prompts ChatGPT to create questions and answers from a text given by a user
    :param str factual_text: A factual text to create questions from
    :returns: A tuple with a string indicating if the actions was successful and if so, also a list
    of tuples containing the questions with the answers  
    """

    prompt: str = \
    f"""I want you to generate a deck of flash cards about the contents of a factual text.
    If the contents of the text violates your TOS or if no text is provided or the text is too 
    short for the task, IGNORE the rest of the prompt and simply reply "I refuse".

    Otherwise, follow the following instructions to the t.

    1. The deck should consist of a single list of tuples that consists of "back":"front" pairs.
    Example:
    [
        ("What is Wikipedia?", "Wikipedia is a free-content online encyclopedia written and maintained by a community of volunteers, collectively known as Wikipedians, through open collaboration."),
        ("What's the capital of Switzerland?", "The capital of Switzerland is called 'Bern'"),
    ]
    2. Remember to also make cards that are not just definitions but connect different concepts together. There should only be whole sentences on the front and the back of the cards.
    3. It is absolutely necessary that you keep the cards in the same language as the text.
    4. There should only be ONE single idea per card. The back of the card should be short and concise.
    5. Do ONLY provide the list of tuples. Your response must start with [ and end with ].

    The text:

    {factual_text}
    """
    # prompter = "Here's a text: \""+bigassstring+"\". Take important terms and make flashcards for them, formated as a list with tuples. Each tuple should contain the selected term and an unique description/meaning/connection as a string. DO NOT FORMAT THE RETURNED STRING - keep it one single line long. If anything goes against your TOS, just say \"I refuse.\"."
    
    message = [ {"role": "user", "content": 
        prompt} ]

    completion = openai.ChatCompletion.create(
        model=MODEL_ENGINE,
        #max_token = 1024,
        #stop=None,
        temperature=0.7,
        messages=message
    )

    response = completion.choices[0].message
    message.append(response)

    #In case something in the generation goes wrong or if text goes against OpenAI's terms of service.
    try:
        res = ast.literal_eval(response.content)
        return True, res
    except SyntaxError:
        message.append({"role": "user", "content": "Why couldn't the flashcards be generated? Explain the reason while using passive voice please."})
        reason = openai.ChatCompletion.create(
            model=MODEL_ENGINE,
            #max_token = 1024,
            #stop=None,
            temperature=0.7,
            messages=message
         ).choices[0].message.content
        return False, reason

# print(get_list("my name is timmy")) # Should return an error. Change to whatever desired text.
