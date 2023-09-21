import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    def __init__(self):
        self.MODE = os.environ.get("MODE")
        self.LOG_LEVEL = os.environ.get("LOG_LEVEL")
        self.SMTP_HOST = os.environ.get("SMTP_HOST")
        self.SMTP_PORT = os.environ.get("SMTP_PORT")
        self.SMTP_USER = os.environ.get("SMTP_USER")
        self.SMTP_PASS = os.environ.get("SMTP_PASS")
        self.REDIS_HOST = os.environ.get("REDIS_HOST")
        self.REDIS_PORT = os.environ.get("REDIS_PORT")
        self.DB_HOST = os.environ.get("DB_HOST")
        self.DB_PORT = os.environ.get("DB_PORT")
        self.DB_NAME = os.environ.get("DB_NAME")
        self.DB_USER = os.environ.get("DB_USER")
        self.DB_PASS = os.environ.get("DB_PASS")

        self.TEST_DB_HOST = os.environ.get("TEST_DB_HOST")
        self.TEST_DB_PORT = os.environ.get("TEST_DB_PORT")
        self.TEST_DB_NAME = os.environ.get("TEST_DB_NAME")
        self.TEST_DB_USER = os.environ.get("TEST_DB_USER")
        self.TEST_DB_PASS = os.environ.get("TEST_DB_PASS")
        self.db_url = (
            f"postgresql+asyncpg://"
            f"{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )
        self.test_db_url = (
            f"postgresql+asyncpg://"
            f"{self.TEST_DB_USER}:{self.TEST_DB_PASS}@{self.TEST_DB_HOST}:{self.TEST_DB_PORT}/{self.TEST_DB_NAME}"
        )
        self.SECRET_KEY = os.environ.get("SECRET_KEY")
        self.ALGORITHM = os.environ.get("ALGORITHM")


settings = Settings()
