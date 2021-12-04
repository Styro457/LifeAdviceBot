import tweepy
import ai
import json
import time

settingsFile = open("twitter-settings.json")
settings = json.load(settingsFile)

print("Starting...")

client = tweepy.Client(
    consumer_key=settings['api_key'],
    consumer_secret=settings['api_key_secret'],
    access_token=settings['access_token'],
    access_token_secret=settings['access_token_secret'],
    wait_on_rate_limit=True
)

minutesLeft = settings['mins_between_tweets']

while True:
    for i in range(0, settings['mins_between_tweets']):
        print(str(minutesLeft) + " minutes left until the next tweet")
        minutesLeft -= 1
        time.sleep(60)
    print("Generating advice...")
    advice = ai.generate_advice()
    print("Tweeting...")
    client.create_tweet(text=advice)
    print("Successfully Tweeted: " + advice)
    minutesLeft = settings['mins_between_tweets']
