import openai
import json
import ast
from dotenv import load_dotenv
from os import environ, path

basedir = path.abspath(path.dirname(__file__))

load_dotenv(path.join(basedir, '.env'))
openai.api_key = environ.get("OPENAIAPIKEY")

model_engine = "gpt-3.5-turbo"
message = [ {"role": "user", "content": 
             " helpful assistant."} ]


def get_list(bigassstring):
    """
    Takes one big string with assorted terms (do not use commas) and makes ChatGPT generate one list with tuples as a string.
    The string is then transformed into a list, which is then returned.
    """
    prompter = "Here's a text: \""+bigassstring+"\". Take important terms and make flashcards for them, formated as a list with tuples. Each tuple should contain the selected term and an unique description/meaning/connection as a string. DO NOT FORMAT THE RETURNED STRING - keep it one single line long. If anything goes against your TOS, just say \"I refuse.\"."
    message = [ {"role": "user", "content": 
        prompter} ]

    completion = openai.ChatCompletion.create(
        model=model_engine,
        #max_token = 1024,
        #stop=None,
        temperature=0.7,
        messages=message
    )

    #In case something in the generation goes wrong or if text goes against OpenAI's terms of service.
    try:
        stringA = completion.choices[0].message.content
        res = ast.literal_eval(stringA)
        return res
    except:
        return "No flaschards can be generated. Please try again or revise your content."

print(get_list("Japanese pornstar")) #Should return an error. Change to whatever desired text.
