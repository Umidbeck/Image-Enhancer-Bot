from aiogram import types

from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, InputFile, ReplyKeyboardRemove

from keyboards.default.info_bot import menuInfo
from keyboards.default.menuKeyboard import menu

from loader import dp

info = "ℹ Bu bot suratlarda 🏞 odamning yuzini aniqlab uni tabiiy ravishda suratda yaxshilash uchun yaratildi. Botdan foydalaninsh oson unga  faqat surat 🌅 yuborsangiz yitarli bot unga ishlov berganidan so'ng sizga natija qaytaradi bu surat sifatiga va unda aks ettirilgan odamlarning soniga qarab bir oz vaqt olishi mumkin.\n "
info += "🛑 Bazida o'zingiz yuborga suratlardan g'ayritabiiy natijalar olishingiz mumkin. Bunga quyidagilar sabab bo'ladi:\n"
info += "🧐 Surat sifati o'ta yomon bo'lsa...\n"
info += "🤭 Suratda inson yuzi to'liq aks etmagan bo'lsa \n"
info += "🤨 Va yana shunday bir qancha sabablar siz kutgan natjani ola olmasligingizga sabab bo'lishi mumkin... \n"
info += "👮‍♂️  Eng asosiy qoidalardan biri bot faqat 'jpg'  vs  'png' farmatidagi suratlarni qabul qiladi.\n"
info += "👨‍🎓 Tavsiyalar :\n"
info += "❗️ Iloji boricha bir suratni takroran botga kiritmang bu surat sifatiga va natija tasir qilishi mumkin.\n"
info += "⁉️ -- Sizning so'rov amalga oshmadi -- bu javobni olishingizga asosiy sabablar: \n"
info += "1️⃣ Surat sifati o'ta past... \n"
info += "2️⃣ Surat hajmi o'ta yuqori...\n"
info += "3️⃣ Surat formati to'gri kelmasligi...\n"
info += "🔢 Bir vaqtta ko'plab suratlar yuborishingiz va hokazo shunga o'xshash hodisalar bu natijani olishingizga sabab bo'lishi mumkin...\n"
info += " \n"
info += " \n"
info += "👨‍💻 P/S: Shunchaki surat jo'nating bo'ldi. \n"


@dp.message_handler(Command('menu'))
async def show_menu(message: Message):
    await message.answer("Start", reply_markup=menu)


@dp.message_handler(text='Bot haqida 🤖')
async def info_show(message: Message):
    await message.answer(text=info, reply_markup=menuInfo)


@dp.message_handler(text='Ortga 🔙')
async def info_show(message: Message):
    await message.answer('Info', reply_markup=menu)


@dp.message_handler(text='Misollar 🌄')
async def info_show(message: Message, album=None):
    album = types.MediaGroup()
    rasm = InputFile(path_or_bytesio="natija/456_00.png")
    rasm1 = InputFile(path_or_bytesio="natija/file_1_09.png")
    album.attach_photo(photo=rasm, caption='Siz yuborgamrasimlar')
    album.attach_photo(photo=rasm1, caption='Siz yuborgamrasimlar')
    await message.reply_media_group(media=album)
