from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
import random 
import asyncio

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

num = random.randint(1, 3)

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Я загадал число от 1 до 3. Угадай!")

@dp.message(F.text == "1")
async def guess_one(message: Message):
    if num == 1:
        await message.reply("Правильно, вы отгадали!")
        await message.answer_photo('https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg')
    else:   
        await message.reply("Неправильно, вы не отгадали.")
        await message.answer_photo('https://media.makeameme.org/created/sorry-you-lose.jpg')

@dp.message(F.text == "2")
async def guess_two(message: Message):
    if num == 2:
        await message.reply("Правильно, вы отгадали!")
        await message.answer_photo('https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg')
    else:
        await message.reply("Неправильно, вы не отгадали.")
        await message.answer_photo('https://media.makeameme.org/created/sorry-you-lose.jpg')

@dp.message(F.text == "3")
async def guess_three(message: Message):
    if num == 3:
        await message.reply("Правильно, вы отгадали!")
        await message.answer_photo('https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg')
    else:
        await message.reply("Неправильно, вы не отгадали.")
        await message.answer_photo('https://media.makeameme.org/created/sorry-you-lose.jpg')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
