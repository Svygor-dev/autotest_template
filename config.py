import os


class Config:

    REQRES_API_URL = None

    @classmethod
    def init_config(cls):
        cls.REQRES_API_URL = os.environ.get("REQRES_API_URL")
