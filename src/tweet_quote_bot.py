import os
import time
import tweepy
import logging
import requests

from config import *
from api import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def get_random_quote(quotes_api_url, quotes_api_key):
    """ Get a random quote from quotes api. """
    headers = {"Authorization": "Bearer {}".format(quotes_api_key)}
    res = requests.get(quotes_api_url + "/quotes/random", headers=headers)
    data = res.json()
    return data


def format_random_quote(quote):
    """ Format a random quote for display. """
    content = quote["quote_text"]
    author = quote["author_name"].strip(",")
    tags = " ".join(["#" + tag for tag in quote["tags"]])
    random_quote = "{}\n\u2014 {}\n{}".format(content, author, tags)
    return random_quote


def tweet_quote_of_the_day(api, quotes_api_url, quotes_api_key):
    try:
        logger.info("Tweeting quote of the day.")
        quote = get_random_quote(quotes_api_url, quotes_api_key)
        status = format_random_quote(quote)
        api.update_status(status=status)
    except:
        logger.error("Error on quote of the day tweet", exc_info=True)


def main():
    quotes_api_url = os.getenv("QUOTES_API_URL")
    quotes_api_key = os.getenv("QUOTES_API_KEY")
    api = create_api()

    while True:
        tweet_quote_of_the_day(api, quotes_api_url, quotes_api_key)
        logger.info("Waiting...")
        time.sleep(60 * 60 * 12)


if __name__ == "__main__":
    main()
