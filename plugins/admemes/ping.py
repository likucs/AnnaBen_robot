"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "🛸✨NASA🚀wale 👨‍🔬🔭 bohot 😳🐋 khatarnak⚠️😱 hain 🆘⛔ 12⏱️ August 🗓️2018 ⏳⏳ko NASA🛩️ne ek spacecraft 🛸launch🚀 kia aur sabhi ko bola 🗣️hum isse sooraj🌞 ki sateh⭕ ko chooh🤌 kar dekhna🙈 chahte hai lekin sachai🙊 kuch aur thi. Jis samay ⏱️ yeh space craft🛸 launch🚀 ho raha tha uss samay Nasa 🛩️ke vigyaniko👨‍🔬 ne iske andar ek dabba 📭rakhdia tha.uss dabbe📭 ke andar ek bidi🚬 rakhi hui thi. Vigyanik👨‍🔬 dekhna👀 chahte the ke sooraj 🌞bidi🚬 ko jala 🔥paata hai ya nahi. Jab yeh sooraj 🌞ki oopri atmosphere🌐 corona 👾mein pohncha to kudrati🏞️ ye bidi🚬 jal 🔥gayi aur NASA🛩️ ne bidi🚬 Mission🚀 mein safal🏆 hokar itihaas 📚rach ke rakhdia💪"
HELP = "ദൈവമേ എന്നെ മാത്രം രക്ഷിക്കണേ...."
REPO = "Check- @cs_repo"
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("help", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_text(HELP)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("repo", COMMAND_HAND_LER) & f_onw_fliter)
async def repo(_, message):
    await message.reply_text(REPO)
