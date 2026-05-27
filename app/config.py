from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8')
    anthropic_api_key : str
    model_name : str = "claude-sonnet-4-5"

settings = Settings()

