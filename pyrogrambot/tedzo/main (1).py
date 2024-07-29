from vars import *
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton




@Bot.on_message(
    filters.channel & (
        filters.text |
        filters.audio |
        filters.document |
        filters.photo |
        filters.sticker |
        filters.video |
        filters.animation |
        filters.voice |
        filters.video_note |
        filters.contact |
        filters.location |
        filters.venue |
        filters.poll |
        filters.game
    )
)
async def autopost(_, message):

    if (len(FROM_CHANNELS) == 0) or (len(TO_CHATS) == 0) or (message.chat.id not in FROM_CHANNELS):
        return

    if not (
        (
            message.text and FILTER_TEXT
        ) or (
            message.audio and FILTER_AUDIO
        ) or (
            message.document and FILTER_DOCUMENT
        ) or (
            message.photo and FILTER_PHOTO
        ) or (
            message.sticker and FILTER_STICKER
        ) or (
            message.video and FILTER_VIDEO
        ) or (
            message.animation and FILTER_ANIMATION
        ) or (
            message.voice and FILTER_VOICE
        ) or (
            message.video_note and FILTER_VIDEO_NOTE
        ) or (
            message.contact and FILTER_CONTACT
        ) or (
            message.location and FILTER_LOCATION
        ) or (
            message.venue and FILTER_VENUE
        ) or (
            message.poll and FILTER_POLL
        ) or (
            message.game and FILTER_GAME
        )
    ):
        return
    
    try:
        for chat_id in TO_CHATS:
            if AS_FORWARD:
                await message.forward(chat_id=chat_id)
            else:
                if REPLY_MARKUP:
                    await message.copy(
                        chat_id=chat_id,
                        reply_markup=message.reply_markup
                    )
                else:
                    await message.copy(chat_id=chat_id)

    except Exception as error:
        print(error)


Bot.run()
