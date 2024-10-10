from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuInfo = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Misollar 🌄'),
            KeyboardButton(text='Ortga 🔙'),
        ],
    ],
    resize_keyboard=True
)
