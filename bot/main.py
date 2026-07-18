import asyncio

from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Bot, Dispatcher
from config import config

from handlers import start


dp = Dispatcher()


async def main() -> None:
    bot = Bot(token=config.telegram.bot_token.get_secret_value())

    dp.include_router(start.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
