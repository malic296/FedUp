import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ["SECRET_KEY"]
    API_URL = os.environ["API_URL"]

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    DEBUG = False

configs = {
    "dev": DevConfig,
    "prod": ProdConfig
}