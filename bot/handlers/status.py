from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import RichBlockTable, RichBlockTableCell, RichTextUnion, RichText

router = Router()


@router.message(Command("status"))
async def start(
    message: Message,
):
    await message.reply("Status")