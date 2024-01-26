from telethon import TelegramClient, events

import openpyxl

from bot_profile import *


# запуск бота
bot = TelegramClient('khorovod', api_id, api_hash).start(bot_token=bot_token)

# бот начинает работу по команде /start
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
    # Создаем список участников
    user_list = []
    for user in all_participants:
            if user.username:
                username = 'https://t.me/' + user.username
            else:
                username = ""
            user_list.append(username)
        
    # Заносим список участников в лист
    
    for i, mbr in enumerate(user_list):
         ws.append({1:i+1, 2:mbr})

    await event.respond("Сохраняем лист...")
    wb.save('member.xlsx')
    await event.respond("Сохраняем файл...")


with bot:
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()
