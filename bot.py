import logging
import asyncio
from telethon import TelegramClient, events, Button
from decouple import config
from telethon.tl.functions.users import GetFullUserRequest

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.INFO)

# start the bot
print("Starting...")
apiid = config("APP_ID", cast=int)
apihash = config("API_HASH")
bottoken = config("BOT_TOKEN")
suryabot = TelegramClient('bot', apiid, apihash).start(bot_token=bottoken)


@suryabot.on(events.NewMessage(incoming=True, chats=-1001412651756)) 
async def _(event): 
    if not event.is_private:
        try:
            await event.client.send_message(-1001311556665, event.message)
        except:
            print("TO_CHANNEL ID is wrong or I can't send messages there (make me admin).")


print("Bot has started.")
