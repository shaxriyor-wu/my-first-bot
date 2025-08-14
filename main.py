import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, F, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN

bot = Bot(token=TOKEN)

x = Dispatcher()

@x.message(CommandStart())
async def start_buyrugini_ushlash(message: Message) -> None:
    await message.answer(f"Assalomu alaykum hurmatli {html.bold(message.from_user.full_name)}, exo botga xush kelibsiz\nExo bot - siz yozgan narsani ozingizga qaytaradi\n Bot haqida malumot olish uchun: haqida")

@x.message(F.text.lower() == f"haqida")
async def Bot_haqida(message: Message):
    await message.reply(f"BU bot Shaxriyor Karimberdiyev tomonidan ochilgan. ochilish sanasi: 14.08.2025")
@x.message(F.photo)
async def photo(message: Message):
    await message.answer(f"Foro ID si: {message.photo[-1].file_id}")
@x.message()
async def replying_answer(message: Message) -> None:
    await message.send_copy(chat_id=message.chat.id)



async def main() -> None:
    await x.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

