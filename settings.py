from dotenv import load_dotenv
import os

load_dotenv()


def getenv(key):
    return os.getenv(key)
