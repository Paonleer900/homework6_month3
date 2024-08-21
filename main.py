import logging
from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from config import dp, bot
from handlers import commands, echo, quiz, FSM_reg, FSM_online_store, notification, send_products, webapp
from handlers import admin_bot
from db import db_main
from config import admin

admin_ids = [7292069375]
chat_ids = [7292069375]

async def on_startup(_):
    for admin_id in admin_ids:
        await notification.set_scheduler()
        await bot.send_message(chat_id=admin_id, text='Бот включен!')
        await db_main.sql_create()

async def on_shutdown(_):
    for admin_id in admin_ids:
        await bot.send_message(chat_id=admin_id, text='Бот выключен!')

commands.register_commands(dp)
quiz.register_quiz(dp)
FSM_reg.register_fsm(dp)
FSM_online_store.store_fsm(dp)
notification.register_notification(dp)
send_products.register_send_products_handler(dp)
webapp.register_handlers(dp)
admin_bot.register_admin(dp)
echo.register_echo(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
