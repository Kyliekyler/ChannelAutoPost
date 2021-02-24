import logging
import asyncio
from telethon import TelegramClient, events, Button
from os import environ
from telethon.tl.functions.users import GetFullUserRequest

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.INFO)

# start the bot
print("Starting...")
apiid = int(environ.get("APP_ID", None))
apihash = environ.get("API_HASH", None)
bottoken = environ.get("BOT_TOKEN", None)
suryabot = TelegramClient('bot', apiid, apihash).start(bot_token=bottoken)


@suryabot.on(events.NewMessage(incoming=True, chats=-1001412651756)) 
async def _(event): 
    if not event.is_private:
        try:
            await event.client.send_message(-1311556665, event.message)
        except:
            print("TO_CHANNEL ID is wrong or I can't send messages there (make me admin).")


print("Bot has started.")
