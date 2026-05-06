from pydantic import BaseSettings
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent / "api.env")


class Settings:
    database = "test"
    port = "5432"
    user = "test"
    password = "test"
    host = "localhost"
    access_token = "dummy"

settings = Settings()
