from pyrogram import Client
from config import BOT_TOKEN,API_HASH,API_ID
import pyrostep

bot = Client('session/bot', plugins=dict(root='plugins'))
pyrostep.listen(bot)


bot.run()