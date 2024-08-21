from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.exceptions import BadRequest
from config import dp, bot


async def webapp_reply_button(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    youtube = KeyboardButton("Youtube", web_app=types.WebAppInfo(url="https://youtube.com"))
    github = KeyboardButton("Github", web_app=types.WebAppInfo(url="https://github.com"))
    wikipedia = KeyboardButton("Wikipedia", web_app=types.WebAppInfo(url="https://www.wikipedia.org"))
    stackoverflow = KeyboardButton("Stackoverflow", web_app=types.WebAppInfo(url="https://stackoverflow.com"))
    google = KeyboardButton("Google", web_app=types.WebAppInfo(url="https://www.google.com"))

    keyboard.add(youtube, github, wikipedia, stackoverflow, google)

    await message.answer(text='Нажми на кнопки для открытия сайтов', reply_markup=keyboard)


async def pin_message(message: types.Message):
    if message.chat.type in ['group', 'supergroup']:
        if message.reply_to_message:
            try:
                await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
                await message.answer("Сообщение закреплено.")
            except BadRequest as e:
                await message.answer(f"Ошибка при закреплении сообщения: {e}")
        else:
            await message.answer("Команда должна быть ответом на сообщение, которое вы хотите закрепить.")
    else:
        await message.answer("Здесь команда не работает, работает только в группах.")


def register_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(webapp_reply_button, commands=['website'])
    dispatcher.register_message_handler(pin_message, commands=['pin'])


register_handlers(dp)
