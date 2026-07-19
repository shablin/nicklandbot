from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_menu() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()

    kb.add(
        InlineKeyboardButton(text="📊 Статус сервера", callback_data="status"),
        InlineKeyboardButton(text="🟢 Онлайн", callback_data="online"),
    )

    kb.adjust(2, 1)

    return kb.as_markup()