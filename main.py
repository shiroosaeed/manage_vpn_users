from pyrogram import Client
from config import BOT_TOKEN,API_HASH,API_ID
import pyrostep
# plugins=dict(root='plugins')
bot = Client('session/bot', plugins=dict(root='plugins'))
pyrostep.listen(bot)


bot.run()