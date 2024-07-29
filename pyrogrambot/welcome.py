from pyrogram import Client, filters
MENTION = "[{}](tg://user?id={})"
MESSAGE = "{} Welcome to [Pyrogram](https://docs.pyrogram.ml/)'s group chat {}!"

chats_filter = filters.chat(["PyrogramChat", "PyrogramLounge"])


@Client.on_message(chats_filter & filters.new_chat_members)
def welcome(client, message):
    new_members = [MENTION.format(i.first_name, i.id) for i in message.new_chat_members]
    text = MESSAGE.format(hyy, ", ".join(new_members))
    message.reply(text, disable_web_page_preview=True)
