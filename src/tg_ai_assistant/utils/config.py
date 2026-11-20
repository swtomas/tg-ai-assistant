from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: str
    ADMIN: int

    model_config = SettingsConfigDict(env_file='files/.env', env_file_encoding='utf-8')


config = Settings(**{})

bot = Bot(token=config.BOT_TOKEN,
          default=DefaultBotProperties(
              parse_mode="HTML"
          )
          )

dp = Dispatcher()

def admin_check(admin_id: int) -> bool:
    return admin_id == config.ADMIN
