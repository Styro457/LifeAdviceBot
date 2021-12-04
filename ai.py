import openai
from pathlib import Path
import json

settingsFile = open("settings.json")
settings = json.load(settingsFile)

openai.organization = settings["openai_org"]
openai.api_key = settings["openai_key"]

prompt = Path('prompt.txt').read_text()

def generate_advice():
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=settings["temperature"],
        max_tokens=settings["max_tokens"],
        stop="\n",
        presence_penalty=settings["presence_penalty"],
        frequency_penalty=settings["frequency_penalty"]
    )
    advice = response.get("choices")[0].get("text")
    for blacklistedWord in settings["blacklistedWords"]:
        if blacklistedWord in advice.lower():
            return generate_advice()
    return advice