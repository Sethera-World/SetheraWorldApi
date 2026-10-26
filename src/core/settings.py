from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    NAME: str
    DESCRIPTION: str
    VERSION: str
    ROOT_PATH: str
    
    model_config = SettingsConfigDict(env_file='.env')