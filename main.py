from telethon import TelegramClient, events

import openpyxl

from bot_profile import *


# запуск бота
bot = TelegramClient('khorovod', api_id, api_hash).start(bot_token=bot_token)


@bot.on(events.NewMessage(pattern='/start'))
async def main(event):
    await event.respond("Привет")
    chat = await event.get_chat()
    await event.respond("Узнаем пользователей...")
    all_participants = []
    all_participants = await bot.get_participants(chat)
    
    # Создаем экземпляр пустой книги Excel
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Список участников"
    #ws.append(("username"))
    user_list = []
    for user in all_participants:
            if user.username:
                username = user.username
            else:
                username = ""
            user_list.append(username)
    ws.append(user_list)
    await event.respond("Сохраняем лист...")
    wb.save('member.xlsx')
    await event.respond("Сохраняем файл...")



with bot:
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()
