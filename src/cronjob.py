import os
from apscheduler.schedulers.blocking import BlockingScheduler

from quote_bot import tweet_quote_of_the_day
from api import create_api


# Create an instance of scheduler and add function
scheduler = BlockingScheduler()


@scheduler.scheduled_job("cron", hour=12)
def scheduled_qotd():
    quotes_api_url = os.getenv("QUOTES_API_URL")
    quotes_api_key = os.getenv("QUOTES_API_KEY")

    api = create_api()
    tweet_quote_of_the_day(api, quotes_api_url, quotes_api_key)


scheduler.start()