from telethon import TelegramClient, events

import openpyxl

from bot_profile import *


# запуск бота
bot = TelegramClient('khorovod', api_id, api_hash).start(bot_token=bot_token)


async def main(event):
    chat = await event.get_chat()



with bot:
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()
