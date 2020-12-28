# Quotes-Twitter-Bot

## :book: Description
Twitter bot for daily quotes

### :darts: Features
- Tweet Scheduling

### :high_brightness: Visuals
![](img/twitter_bot.png)

## :bulb: Getting Started
Follow the instructions below to work on the project on your local environment.

### :clipboard: Prerequisites
You'll need Git, Python 3.8, Pip and a Virtual Environment (in this case, Pipenv is used as a package manager and virtual environment).

### :computer: Installation
```
# Clone this repository
$ git clone https://github.com/miguel-osuna/Quotes-Twitter-Bot.git

# Go into the repository from the terminal
$ cd Quotes-Twitter-Bot

# Remove current origin repository
$ git remote remove origin

# Install dependencies
$ pipenv install

# Run the project
$ python3 src/cronjob.py
```
All dependencies are listed on the Pipfile.

## :rocket: Deployment
This project includes a Procfile for Heroku, but can be deployed to any other host.
- Heroku: read the [following tutorial](https://devcenter.heroku.com/articles/getting-started-with-python) to learn how to deploy to your heroku account..

## :wrench: Built With
- [tweepy](https://docs.tweepy.org/en/latest/)

## :performing_arts: Authors
- **Miguel Osuna** - https://github.com/miguel-osuna

## :ledger: License
This project is licensed under the MIT License - see the LICENSE.md file for details.
