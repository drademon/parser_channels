import asyncio
import time
from pyrogram import Client
from datetime import datetime, timedelta


#api_id = 11111111
#api_hash = 'XXXXXXXXXXXXXXXXXXXX'
name_session_file = "my_account"
chat_url = "@tovari_waldberries"
input_day = ''

while True:
    try:
        input_day = int(input("Введите период (дней):"))
    except:
        print("Введено не число")
    else:
        break

date_period = datetime.today() - timedelta(days=input_day)
list_names = []
open("names.txt", "w")


async def main():
    async with Client(name_session_file) as app:
        chat = await app.get_chat(chat_url)
        chat_id = chat.id
        print(date_period)
        async for message in app.get_chat_history(chat_id, limit=1000):
            if message.date > date_period:
                if message.caption:
                    try:
                        mes_ls = message.caption.split("@")[1].split(" ")[0].split("\n")[0].replace(",", "").replace(
                            "\xa0", '')
                        time.sleep(1)
                        list_names.append("@"+mes_ls)
                    except Exception as error:
                        print(error)
            else:
                break
    with open("names.txt", "a", encoding="utf-8") as docs:
        docs.write('\n'.join(list_names))


asyncio.run(main())
