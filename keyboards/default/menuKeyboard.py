from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Bot haqida 🤖')
        ],
    ],
    resize_keyboard=True
)
