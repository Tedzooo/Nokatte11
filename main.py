from pyrogram import Client, filters 
import asyncio
import os
from dotenv import load_dotenv
API_ID = '15453419'
API_HASH = '6c9c9e5a2e65daf192e7dd9dde026f45'
BOT_TOKEN = '7161717671:AAF4VBmLu3JGECaPXMdVPxrawt3SrE0LbcQ'
# Define a list of prank messages

# Initialize the Clien
group_id = -1002006186805
load_dotenv()

app= Client(
    "Pyrogram Bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    workers=100,
    plugins=dict(root="pyrogrambot")
)

@app.on_message(filters.chat(group_id) & ~filters.me)
async def process_message(client, message):
    try:
        text = message.text.lower()
        if text in ['hi', 'hello']:
            sent_message = await message.reply("Hello there, welcome to community.")
            print(f"Message sent successfully: {sent_message.text}")
    except Exception as e:
        print(f"Failed to send message: {e}")

async def main():
    try:
        await app.start()
        print("Bot started")
        # Keep the bot running
        while True:
            await asyncio.sleep(10)
    except Exception as e:
        print(f"Error starting bot: {e}")
    finally:
        await app.stop()
app.run()
