from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters import Command
import logging, asyncio
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

start_buttons = [
    [types.KeyboardButton(text='Курсы'), types.KeyboardButton(text='О нас'), ],
    [types.KeyboardButton(text='Адрес'), types.KeyboardButton(text='Контакты')],
]

start_keyboard = types.ReplyKeyboardMarkup(keyboard=start_buttons, resize_keyboard=True)

course = [
    [types.KeyboardButton(text='Backend'), types.KeyboardButton(text='Frontend')],
    [types.KeyboardButton(text='Android'), types.KeyboardButton(text="UX/UI")],
    [types.KeyboardButton(text='Оставить заявку'), types.KeyboardButton(text='Назад')]
]

courses_keyboard = types.ReplyKeyboardMarkup(keyboard=course, resize_keyboard=True)
#ReplyKeyboardMarkup — объект, представляющий клавиатуру, которая отображается под полем ввода текста у пользователя в Telegram.

#keyboard — добавляет все кнопки из списка start_buttons на клавиатуру.

@dp.message(Command("start"))
async def start(message:Message):
    await message.answer(f'Здравствуйте {message.from_user.full_name}', reply_markup=start_keyboard)
    
@dp.message(F.text == 'О нас')
async def about_us(message:Message):
    await message.reply("Geeks - это айти курсы в Оше, Кара-Балте, Бишкеке основанное 2018г")
    
@dp.message(F.text == "Адрес")
async def location(message:Message):
    await message.reply_location(latitude=40.51931846586533, longitude=72.80297788183063)
    
@dp.message(F.text == "Контакты")
async def contact(message:Message):
    await message.reply_contact(phone_number='+996505180600', first_name='isko', last_name='isko')
    
@dp.message(F.text == 'Курсы')
async def course(message:Message):
    await message.reply('Вот наши курсы:', reply_markup=courses_keyboard)    
    
@dp.message(F.text == 'Backend')
async def back(message:Message):
    await message.reply("Backend - это серверная сторона сайта или приложения. В основном код вам не виден")
    
@dp.message(F.text == 'Frontend')
async def front(message:Message):
    await message.reply("Frontend - это лицевая сторона сайта или приложения. Эту часть вы можете видеть")
    
@dp.message(F.text == 'Android')
async def android(message:Message):
    await message.reply("Android - это разработка мобильного приложения. С ОС Android")
    
@dp.message(F.text == 'UX/UI')
async def uxui(message:Message):
    await message.reply("UX/UI - это дизайн сайта или приложения.")
    
@dp.message(F.text == 'Назад')
async def backi(message:Message):
    await message.answer("Вы вернулись в главное меню", reply_markup=start_keyboard)
    
@dp.message(F.text == 'Оставить заявку')
async def application(message:Message):
    buuton = [[types.KeyboardButton(text='Отправить заявку', request_contact=True)]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=buuton, resize_keyboard=True)
    await message.reply("Пожалуйста, отправьте свои контактные данные", reply_markup=keyboard)
    
@dp.message(F.contact)
async def get_conatct(message:Message):
    contact_info = f'Заявка на курсы \nИмя: {message.contact.first_name}\nФамилия: {message.contact.last_name}\nТелефон: {message.contact.phone_number}'
    await bot.send_message(chat_id=-4255458461, text=contact_info)
    await message.answer("Спасибо, что оставили заявку")
    await message.answer('Вы вернулись на главное меню', reply_markup=start_keyboard)
    
async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())
