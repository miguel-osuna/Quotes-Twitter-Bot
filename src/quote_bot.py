from datetime import datetime
import tweepy
import logging
import requests

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
    content = '"{}"'.format(quote["quote_text"])
    author = quote["author_name"].strip(",")
    tags = " ".join(["#" + tag for tag in quote["tags"]])
    random_quote = "{}\n\u2014 {}\n{}".format(content, author, tags)
    return random_quote


def tweet_quote_of_the_day(api, quotes_api_url, quotes_api_key):
    """ Tweets a quote of the day status for the api app account. """
    try:
        logger.info("Tweeting quote of the day. Time is {}".format(datetime.now()))
        quote = get_random_quote(quotes_api_url, quotes_api_key)
        status = format_random_quote(quote)

        tweet_max_lenght = 280
        if len(status) < tweet_max_lenght:
            api.update_status(status=status)

        else:
            logger.info("Tweet exceeds max length. Getting new quote.")
            tweet_quote_of_the_day(api, quotes_api_url, quotes_api_key)

    except Exception as e:
        logger.error("Error on quote of the day tweet", exc_info=True)
        raise e
