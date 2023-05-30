from pyrogram import Client, filters 
from pyrogram.types import ReplyKeyboardMarkup
import pyrostep
from helpers.ovpn_manager import Ovpn
config={
 "username":"",
 "password":"",
}
   

ovpn=Ovpn()


@Client.on_message(filters.command('start'))
def starting(c,m):
    btn = ReplyKeyboardMarkup([
       ['add account']

    ],resize_keyboard=True)

    m.reply('select a butn',reply_markup=btn)

@Client.on_message(filters.regex('add account'))
async def add_account(c,m):
    await m.reply('send user name')
    await pyrostep.register_next_step(m.from_user.id,set_username)
async def set_username(c,m):
    config['username']=m.text
    await m.reply('send password')
    await pyrostep.register_next_step(m.from_user.id,set_password)
async def set_password(c,m):
    config['password']=m.text
    ovpn.create_user(config)
    await m.reply('user created succsessfuly')

        



