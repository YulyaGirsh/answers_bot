from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State

from config import TOKEN
import logging
from keyboards import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from texts import *

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
ID = '1111'


class ProfileStatesGroup(StatesGroup):
    photo = State()
    lesson = State()
    mail = State()


@dp.message_handler(Text(equals='ГЛАВНОЕ МЕНЮ'))
async def main_menu(message: types.Message):
    await message.answer('⬇️ГЛАВНОЕ МЕНЮ⬇️', reply_markup=menu_kb)
    await message.delete()


@dp.callback_query_handler()
async def guarantee(callback: types.CallbackQuery):
    if callback.data == 'guarantee':
        await callback.message.answer(garantee, reply_markup=back_menu)
    elif callback.data == 'dop_info':
        await callback.message.answer(dop1)
        await callback.message.answer(dop2)
        await callback.message.answer(dop3, reply_markup=back_menu)
    elif callback.data == 'back':
        await callback.message.answer('⬇️ГЛАВНОЕ МЕНЮ⬇️', reply_markup=menu_kb)
    elif callback.data == 'payment':
        await callback.message.answer("ЦЕНА ДОСТУПА В ОДНУ ГРУППУ:\n🔹ЕГЭ - 1199 рублей.\n🔹ОГЭ - 899 "
                                      "рублей.\n🔹Итоговое сочинение - 599₽\n🔹Итоговое собеседование 499₽\n⚠️На каждый "
                                      "предмет отдельная группа\n⚠️Каждая группа оплачивается отдельно",
                                      reply_markup=pay_menu)
    elif callback.data == 'ege':
        await callback.message.answer('Здесь вы можете выбрать нужный вам предмет! ЕГЭ⬇️', reply_markup=ege_lessons_ikb)
    elif callback.data == 'oge':
        await callback.message.answer('Здесь вы можете выбрать нужные вам предметы!', reply_markup=ege_lessons_ikb)
    elif callback.data == 'sochen':
        await callback.message.answer(otvet, reply_markup=start_fsm)
    elif callback.data == 'sobes':
        await callback.message.answer(otvet, reply_markup=start_fsm)
    elif callback.data == 'postoplata':
        await callback.message.answer(otvet, reply_markup=start_fsm)


@dp.message_handler(commands=['take_answers'])
async def send_create(message: types.Message):
    await message.answer("Теперь отправь нам скриншот чека об оплате!")
    await ProfileStatesGroup.photo.set()


@dp.message_handler(lambda message: not message.photo, state=ProfileStatesGroup.photo)
async def check_photo(message: types.Message):
    await message.reply('Это не скриншот!')


@dp.message_handler(content_types='photo', state=ProfileStatesGroup.photo)
async def get_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await message.answer('Теперь укажи предмет, на который ты хочешь получить ответы!\n'
                         'Если ты оплатил итоговое сочинение или итоговое собеседование, то так и напиши!')
    await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.lesson)
async def get_mail(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['lesson'] = message.text
    await message.answer('Теперь укажи свой email!')
    await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.mail)
async def get_mail(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['mail'] = message.text
    await bot.send_photo(ID, photo=data['photo'], caption=data['mail'] + '\n' + data['lesson'])
    await message.answer('Жди сообщения на почту! Скоро тебе отправят все материалы!')
    await state.finish()


@dp.message_handler(commands=['start'])
async def send_start(message: types.Message):
    await message.answer(welcome,
                         reply_markup=start_kb)
    await message.delete()


@dp.message_handler(commands=['cancel'], state='*')
async def cmd_cancel(message: types.Message, state: FSMContext):
    if state is None:
        return

    await state.finish()
    await message.reply('Вы прервали отправку')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
