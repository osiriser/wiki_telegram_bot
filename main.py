import asyncio

from wikipediaapi import Wikipedia
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart

from assets.config import * 

wiki = Wikipedia(language="en", user_agent="Your_User_Agent_String")
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    if message.chat.type != "private":
        await message.reply(no_group)
        return
    
    await message.answer_photo(
        photo="https://te.legra.ph/file/72e602045e29a0f5ec882.jpg",
        caption=start_text,
    )


@dp.message(F.text)
async def wwiki(message: Message):
    if message.chat.type != "private":
        await message.reply(no_group)
        return
    
    query = message.text
    page = wiki.page(query)
    msg = await message.answer("🔎 <b>Search for information...</b>")
    await asyncio.sleep(0.5)
    if page.exists():
        await message.answer(f"<b>🌐 {page.title}:\n\n{page.summary}\n\n<b>All information:</b> -> <a href='{page.fullurl}'>Click</a></b>")
        await msg.delete()
    else:
        await message.reply("🚫 <b>Unfortunately, I was unable to find information on this request.</b>")
        await msg.delete()


async def main():
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Bot started!")
    try:
        asyncio.run(main())
    except Exception as e:
        print(e)
