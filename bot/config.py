from pydantic import SecretStr, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class TelegramConfig(BaseModel):
    bot_token: SecretStr
    admin_ids: list[int]
    broadcast_chat: int


class MinecraftConfig(BaseModel):
    host: str = "localhost"
    port: int = 25565


class RCONConfig(BaseModel):
    port: int = 25575
    password: SecretStr


class Settings(BaseSettings):
    telegram: TelegramConfig
    minecraft: MinecraftConfig
    rcon: RCONConfig

    model_config = SettingsConfigDict(
        env_file=".env", env_nested_delimiter="__", env_file_encoding="utf-8"
    )


config = Settings()
