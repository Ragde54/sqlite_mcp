from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    database_path: str = Field(default="data/dev.db", validation_alias="DATABASE_PATH")
    read_only: bool = Field(default=False, validation_alias="READ_ONLY")
    server_name: str = Field(
        default="habit-tracker-mcp", validation_alias="SERVER_NAME"
    )


settings = Settings()
