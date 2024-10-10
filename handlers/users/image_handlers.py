import os
import shutil
from pathlib import Path

from aiogram import types

from loader import dp
from aiogram.types import ContentTypes, Message, InputFile

# from utils.gfpgan.GFPGAN import inputs
from utils.inference_gfpgan import main

downloads_path = Path().joinpath("downloads", "categories")
downloads_path.mkdir(parents=True, exist_ok=True)


@dp.message_handler(content_types=ContentTypes.PHOTO)
async def photo_handler(message: Message):
    try:
        k = await message.photo[-1].download(destination_dir=downloads_path)
        # img = await bot.get_file(photos)
        # result: io.BytesIO = await bot.download_file(img)
        # name = os.path.basename(photo)
        await message.answer('Rasim qabul qilindi 👨‍💻')
        # if os.path.isdir(upload_folder):
        #     shutil.rmtree(upload_folder)
        # os.mkdir(upload_folder)
        results = await main(k)
        image_url = f"results/restored_imgs/{results}_00.png"
        upload_folder_01 = image_url
        image_url_2 = f'results/restored_imgs/{results}_01.png'
        upload_folder_02 = image_url_2
        image_url_3 = f'results/restored_imgs/{results}_02.png'
        upload_folder_03 = image_url_3
        image_url_4 = f'results/restored_imgs/{results}_03.png'
        upload_folder_04 = image_url_4
        image_url_5 = f'results/restored_imgs/{results}_04.png'
        upload_folder_05 = image_url_5
        album = types.MediaGroup()
        photo_1 = InputFile(path_or_bytesio=f"results/restored_imgs/{results}.jpg")
        if os.path.isfile(upload_folder_01):
            photo_2 = InputFile(path_or_bytesio=f"results/restored_imgs/{results}_00.png")
        if os.path.isfile(upload_folder_02):
            photo_3 = InputFile(path_or_bytesio=f"results/restored_imgs/{results}_01.png")
        if os.path.isfile(upload_folder_03):
            photo_4 = InputFile(path_or_bytesio=f"results/restored_imgs/{results}_02.png")
        if os.path.isfile(upload_folder_04):
            photo_5 = InputFile(path_or_bytesio=f"results/restored_imgs/{results}_03.png")
        if os.path.isfile(upload_folder_05):
            photo_6 = InputFile(path_or_bytesio=f"results/restored_imgs/{results}_04.png")
        text1 = '📷 Natijalar...⬆️⬆️⬆️\n\n\n 🤖 Bot link: @Img_Enhancer_bot '
        album.attach_photo(photo=photo_1)
        if os.path.isfile(upload_folder_01):
            album.attach_photo(photo=photo_2)
        if os.path.isfile(upload_folder_02):
            album.attach_photo(photo=photo_3)
            # caption = '📷 Natijalar...\n\n\n🤖 Bot link: @Img_Enhancer_bot '
        if os.path.isfile(upload_folder_03):
            album.attach_photo(photo=photo_4)
        if os.path.isfile(upload_folder_04):
            album.attach_photo(photo=photo_5)
        if os.path.isfile(upload_folder_05):
            album.attach_photo(photo=photo_6)
        # upload_folder_2 = 'downloads/categories/photos'
        # if os.path.isdir(upload_folder_2):
        #     shutil.rmtree(upload_folder_2)
        # os.mkdir(upload_folder_2)
        await message.reply_media_group(media=album)
        await message.answer(text=text1)
        # for filename in os.listdir('results/restored_imgs/'):
        #     if filename.startswith(results):
        #         del_file = f"results/restored_imgs/{filename}"
        #         del_file1 = del_file
        #         os.remove(del_file1)
    except:
        msg = "Sizning so'rovingiz amalga oshmadi."
        await message.answer(text=msg)
        for filename in os.listdir('downloads/categories/photos/'):
            del_image = f"<_io.BufferedWriter name='downloads/categories/photos/{filename}'>"
            k1 = f'{k}'
            del_img = del_image
            if k1 == del_img:
                print(1)
                del_file = f"downloads/categories/photos/{filename}"
                del_file1 = del_file
                os.remove(del_file1)


@dp.message_handler(content_types=ContentTypes.ANY)
async def any_handler(message: Message):
    text = "Siz faqat 'png' va 'jpg' formatidagi suratlarni kirita olasiz."
    await message.answer(text=text)
