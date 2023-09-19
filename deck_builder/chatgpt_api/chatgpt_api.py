import openai
import json
import ast


openai.api_key = "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"

model_engine = "gpt-3.5-turbo"
message = [ {"role": "user", "content": 
             " helpful assistant."} ]


def get_list(bigassstring):
    """
    Takes one big string with assorted terms (do not use commas) and makes ChatGPT generate one list with tuples as a string.
    The string is then transformed into a list, which is then returned.
    """
    prompter = "Here's a text: \""+bigassstring+"\". Take important terms and make flashcards for them, formated as a list with tuples. Each tuple should contain the selected term and an unique description/meaning/connection as a string. DO NOT FORMAT THE RETURNED STRING - keep it one single line long."
    message = [ {"role": "user", "content": 
        prompter} ]

    completion = openai.ChatCompletion.create(
        model=model_engine,
        #prompt=prompte,
        #max_token = 1024,
        #stop=None,
        temperature=0.7,
        messages=message
    )

    stringA = completion.choices[0].message.content
    res = ast.literal_eval(stringA)
    return res

print(get_list("Photosynthesis is a biological process used by many cellular organisms to convert light energy into chemical energy, which is stored in organic compounds that can later be metabolized through cellular respiration to fuel the organism's activities."))