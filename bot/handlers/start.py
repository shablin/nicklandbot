from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.menu import main_menu

router = Router()


@router.message(CommandStart())
async def start(
    message: Message,
):
    msg = (
        "Привет! Я смотритель Никляндии. "
        "Пока что я умею мало, но постоянно развиваюсь.\n\n"
        "*Подсказка:*\n"
        "/status - узнать текущий статус сервера\n"
        "/online - подробности об онлайн игроках\n"
        "/go - запустить сервер"
    )

    await message.answer(
        text=msg,
        parse_mode="markdown",
        reply_markup=main_menu()
    )
