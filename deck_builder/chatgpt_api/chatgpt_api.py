import openai
import json
import ast


openai.api_key = "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"

model_engine = "gpt-3.5-turbo"
message = [ {"role": "user", "content": 
             " helpful assistant."} ]


def get_list(bigassstring):
    prompter = "Here are random terms: \""+bigassstring+"\". Generate a list with. Each tuple should contain the term and description or meaning as a string. DO NOT FORMAT THE RETURNED STRING - keep it one single line long."
    message = [ {"role": "user", "content": 
        prompter} ]

    completion = openai.ChatCompletion.create(
        model=model_engine,
        #prompt=prompte,
        #max_toxen = 1024,
        #stop=None,
        temperature=0.5,
        messages=message
    )

    return completion.choices[0].message.content


stringA = get_list("World war one half-life football cow water bottle Cristiano Ronaldo")
res = ast.literal_eval(stringA)
print(res)