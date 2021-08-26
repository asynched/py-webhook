from os import environ
from dotenv import load_dotenv

load_dotenv()

SECRET_AUTHORIZATION_HEADER = environ.get("SECRET_AUTHORIZATION_HEADER")
