from pyrogram import Client, filters 
from pyrogram.types import ReplyKeyboardMarkup
import pyrostep
from helpers.cisco_manage import Cisco
config={
 'username':'',
 'password':'',


}
   




@Client.on_message(filters.command('start'))
def starting(c,m):
    btn = ReplyKeyboardMarkup([
       ['add account']

    ],resize_keyboard=True)

    m.reply('select a butn',reply_markup=btn)

@Client.on_message(filters.regex('add account'))
async def add_account(c,m):
    await m.reply('enter user name')
    await pyrostep.register_next_step(m.from_user.id, set_user_name)

async def set_user_name(c,m):
    config.username=m.text
    await m.reply('enter password')
    await pyrostep.register_next_step(m.from_user.id, set_password)

async def set_password(c,m):
    await m.reply('select vpn core')
    config.password=m.text
    await pyrostep.register_next_step(m.from_user.id, set_vpn_core)

async def set_vpn_core(c,m):
    if m.text=='cisco':
        cisco_vpn=Cisco()

        cisco_vpn.create_user(config.username,config.password)
        await m.reply('user created')

        



