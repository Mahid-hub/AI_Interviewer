from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    groq_api_key: str
    groq_model: str = "openai/gpt-oss-20b"

    qdrant_url: str
    qdrant_api_key: str

    langfuse_public_key: str
    langfuse_secret_key: str
    langfuse_base_url: str




settings = Settings()