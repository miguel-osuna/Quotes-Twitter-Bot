import os
from os.path import dirname, abspath, join

from dotenv import load_dotenv

ENVIRONMENT = "local"
BASE_PROJECT_PATH = dirname(dirname((abspath(__file__))))
ENV_PATH = join(BASE_PROJECT_PATH, ".env")

# Load environment variables
load_dotenv(ENV_PATH)