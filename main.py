from pathlib import Path

import json
import time
import tweepy

import ai

settingsFile = open("settings.json")
settings = json.load(settingsFile)

adviceAI = ai.AI(
    organization=settings['openai_organization'],
    api_key=settings['openai_api_key'],
    prompt=Path('prompt.txt').read_text(),
    temperature=settings['ai_temperature'],
    max_tokens=settings['ai_max_tokens'],
    presence_penalty=settings['ai_presence_penalty'],
    frequency_penalty=settings['ai_frequency_penalty'],
    blacklisted_words=settings['blacklisted_words']
)

print("Starting...")

client = tweepy.Client(
    consumer_key=settings['twitter_api_key'],
    consumer_secret=settings['twitter_api_key_secret'],
    access_token=settings['twitter_access_token'],
    access_token_secret=settings['twitter_access_token_secret'],
    wait_on_rate_limit=True
)

minutesLeft = settings['mins_between_tweets']

while True:
    while minutesLeft > 0:
        print(str(minutesLeft) + " minutes left until the next tweet")
        minutesLeft -= settings['mins_between_time_announcements']
        time.sleep(60 * settings['mins_between_time_announcements'])
    print("Generating advice...")
    advice = adviceAI.generate_advice()
    print("Tweeting...")
    client.create_tweet(text=advice)
    print("Successfully Tweeted: " + advice)
    minutesLeft = settings['mins_between_tweets']
