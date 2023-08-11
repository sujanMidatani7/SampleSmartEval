from dotenv import load_dotenv
from pathlib import Path
import os


def load_env():
    dotenv_path = Path(__file__).parent.parent.parent / '.env'
    print(dotenv_path)
    load_dotenv(dotenv_path=dotenv_path)


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY is None:
    load_env()
