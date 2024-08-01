import requests
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

# Telegram bot tokenini o'rnating
TELEGRAM_TOKEN = '7385548735:AAGF6oj1S65hDMoPqmCHI5fuMnbeKACekA8'

# Bot va Dispatcher ni yaratish
bot = Bot(token=TELEGRAM_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("""Salom! Spotify botiga xush kelibsiz! Artistlar haqida ma'lumot olish uchun 
                        /get_artists - Artistlar ismalari
                        /get_songs - Qo'shiqlar ro'yhati
                        /get_alboms - Albomlar ro'yhati
                        buyrug‘ini yuboring.""")

@dp.message_handler(commands=['get_artists'])
async def get_artists(message: types.Message):
    response = requests.get('http://127.0.0.1:8000/api/artist/')
    if response.status_code == 200:
        artists = response.json()
        if artists:
            for artist,i in zip(artists, range(1, (len(artists)+1))):
                artists_list = artist['first_name']
                await message.reply(f"Qo'shiqchi ismlari:\n{i}. {artists_list}")
        else:
            await message.reply("Qo'shiqchi topilmadi.")
    else:
        await message.reply("Qo'shiqlarni olishda xatolik yuz berdi.")


@dp.message_handler(commands=['get_alboms'])
async def get_alboms(message: types.Message):
    response = requests.get('http://127.0.0.1:8000/api/albom/')
    if response.status_code == 200:
        alboms = response.json()
        if alboms:
            for albom,i in zip(alboms, range(1, (len(alboms)+1))):
                alboms_list = albom['title']
                await message.reply(f"Albomlar nomi:\n{i}. {alboms_list}")
        else:
            await message.reply("Albomlar topilmadi.")
    else:
        await message.reply("Albomlarni olishda xatolik yuz berdi.")

@dp.message_handler(commands=['get_songs'])
async def get_songs(message: types.Message):
    response = requests.get('http://127.0.0.1:8000/api/song/')
    if response.status_code == 200:
        songs = response.json()
        if songs:
            for song,i in zip(songs, range(1, (len(songs)+1))):
                songs_list = song['title']
                await message.reply(f"Qo'shiqlar nomi:\n{i}. {songs_list}")
        else:
            await message.reply("Qo'shiqlar topilmadi.")
    else:
        await message.reply("Qo'shiqlarni olishda xatolik yuz berdi.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
