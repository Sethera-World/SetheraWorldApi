from fastapi import FastAPI
from src.core.settings import Settings

class App(FastAPI):
    def __init__(self, **kwargs):
        settings = Settings()
        super().__init__(**kwargs)
        self.title = settings.NAME
        self.description = settings.DESCRIPTION
        self.version = settings.VERSION
        self.root_path = settings.ROOT_PATH
        

app = App()