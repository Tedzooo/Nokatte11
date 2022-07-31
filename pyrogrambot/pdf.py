import os
from PIL import Image
from pyrogram import Client,filters 
from pyrogram.types import (InlineKeyboardButton,  InlineKeyboardMarkup)

from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant


LIST = {}

@Client.on_message(filters.command(['menu']))
async def start(client, message):
 await message.reply_text(text =f"""Hello {message.from_user.first_name }image to pdf bot 
i can convert image to pdf
This bot created by @tedzosir""",reply_to_message_id = message.message_id ,  reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("movies 🇮🇳" ,url="https://t.me/tedzomovie01") ],
                 [InlineKeyboardButton("update 🧐", url="https://t.me/tzobotz") ]       ]        ) )




@Client.on_message(
    filters.command("telegraph") &
    f_onw_fliter
)
async def pdf(client,message):
 
 if not isinstance(LIST.get(message.from_user.id), list):
   LIST[message.from_user.id] = []

  
 
 file_id = str(message.photo.file_id)
 ms = await message.reply_text("Converting to PDF ......")
 file = await client.download_media(file_id)
 
 image = Image.open(file)
 img = image.convert('RGB')
 LIST[message.from_user.id].append(img)
 await ms.edit(f"{len(LIST[message.from_user.id])} image   Successful created PDF if you want add more image Send me One by one\n\n **if done click here 👉 /convert** ")
 

@Client.on_message(filters.command(['convert']))
async def done(client,message):
 images = LIST.get(message.from_user.id)

 if isinstance(images, list):
  del LIST[message.from_user.id]
 if not images:
  await message.reply_text( "No image !!")
  return

 path = f"{message.from_user.id}" + ".pdf"
 images[0].save(path, save_all = True, append_images = images[1:])
 
 await client.send_document(message.from_user.id, open(path, "rb"), caption = "Here your pdf !!")
 os.remove(path)
