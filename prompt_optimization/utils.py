"""
https://oai.azure.com/portal/be5567c3dd4d49eb93f58914cccf3f02/deployment
clausa gpt4
"""

import time
import requests
import config
import string

from openai import AzureOpenAI

import json

import configparser
config = configparser.ConfigParser()
config.read('../configs/config.ini')

client = AzureOpenAI(
    api_key = config['AZUREOPENAI']['API_KEY'],
    azure_endpoint = config['AZUREOPENAI']['ENDPOINT'],
    api_version = "2023-07-01-preview"
)


def parse_sectioned_prompt(s):

    result = {}
    current_header = None

    for line in s.split('\n'):
        line = line.strip()

        if line.startswith('# '):
            # first word without punctuation
            current_header = line[2:].strip().lower().split()[0]
            current_header = current_header.translate(str.maketrans('', '', string.punctuation))
            result[current_header] = ''
        elif current_header is not None:
            result[current_header] += line + '\n'

    return result


def chatgpt(prompt, temperature=0.7, n=1, top_p=1, stop=None, max_tokens=1024, 
                  presence_penalty=0, frequency_penalty=0, logit_bias={}, timeout=10):
    
    print("running chat completion")
    
    chat_completion = client.chat.completions.create(
        model="utmb-openai-gpt4-32k", # model = "deployment_name".
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        n=n,
        top_p=top_p,
        stop=stop,
        max_tokens=max_tokens,
        presence_penalty=presence_penalty,
        frequency_penalty=frequency_penalty,
        logit_bias=logit_bias
    )

    print(f"chat completion: {chat_completion}")

    r = json.loads(chat_completion.json())
    return [choice['message']['content'] for choice in r['choices']]


def instructGPT_logprobs(prompt, temperature=0.7):
    
    print("running completion")

    completion = client.completions.create(
        model="utmb-openai-gpt4-32k",
        prompt=prompt,
        temperature=temperature,
        max_tokens=1,
        logprobs=1,
        echo=True
    )

    print(f"completion: {completion}")

    r = json.loads(completion.json())
    return r['choices']