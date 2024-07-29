from pyrogram import Client, filters 
import asyncio
import os
from dotenv import load_dotenv
from vars import *


# Initialize the Client


load_dotenv()

app= Client(
    "Pyrogram Bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    workers=100,
    plugins=dict(root="pyrogrambot")
)


app.run()
