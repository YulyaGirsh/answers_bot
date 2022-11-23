from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State

from config import TOKEN
import logging
from keyboards import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

API_TOKEN = 'BOT TOKEN HERE'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
ID = '170481504'


class ProfileStatesGroup(StatesGroup):
    photo = State()
    lesson = State()
    mail = State()


garantee = '1️⃣ В нашей команде работают люди, занимающие высокое положение в данной сфере и они имеют свободный ' \
           'доступ ко всей информации на ОГЭ и ЕГЭ.\n2️⃣ Mы пpeдocтaвляeм вapиaнты и oтвeты зa 20 чacoв дo нaчaлa ' \
           'экзaмeнa.\n 3️⃣ За 30 часов до начала экзамена мы получаем все КИМы на руки и прорешиваем все ' \
           'задания.\n️4️⃣ Мы дорожим своими клиентами и стараемся помочь сдать экзамен.  \n 5️⃣ О нашей команде мало ' \
           'кто знает, т.к. вся информация доступна только избранному кругу людей, оплатившим наши услуги.\n' \
           '6️⃣ Мы ни в коем случае не копируем варианты ответов из других источников.\n' \
           '7️⃣ Мы являемся первоисточником ответов.\n8️⃣ Мы имеем многолетний опыт работы за плечами.\n9️⃣ У нас все честно и без обмана, мы ни в коем случае не хотим обманывать людей которые и так находятся в стрессовом состоянии перед гос. экзаменом.\n' \
           '🔟 Haш пpoeкт пpeдocтaвляeт peaльныe KИMы и oтвeты EГЭ/OГЭ 2022 нa ocнoвную вoлну и peзepвныe cpoки.'
dop1 = '⚠️ КИМы покупаем у определённых лиц из министерства образования, с которыми у нас есть связи. Покупаем без каких-либо посредников. КИМы доступны нам уже за 30 часов до экзамена. Далее скидываем все КИМы Вам (в вип группу). После этого наша команда решает все задания, и через несколько часов мы предоставляем Вам уже готовые ответы на ВСЕ задания.'
dop2 = '⚠️Koнeчнo, ни oдни KИMы нe мoгут чиcтo тeopeтичecки cтoить пapу тыcяч pублeй в oффлaйнe, но рacпpeдeляя вcю ' \
       'cтoимocть нa oпpeдeлeннoe кoличecтвo пoльзoвaтeлeй, мы уcтaнaвливaeм впoлнe paзумныe цeны.' \
       'Даже если вы уверены что сдадите, то я вас уверяю, бывают непредвиденные обстоятельства, когда очень даже ' \
       'умные и образованные ученики не сдавали из-за тех или иных непредвиденных обстоятельств, поэтому советую на всякий случай ПЕРЕСТРАХОВАТЬСЯ и купить ответы. Кстати, эти ответы стоят относительно недорого (например относительно стоимости репетиторов или подготовительных курсов).'
dop3 = '🔶Любыe взaимoдeйcтвия в ceти "интepнeт" дoлжны пoдкpeплятьcя гapaнтиями, будь этo пpoдaжa тoвapoв или oкaзaниe уcлуг. Heвoзмoжнo быть увepeнными в тoм, чтo нa дpугoм кoнцe cтpaны тoвap, кoтopый Bы зaкaзaли, дeйcтвитeльнo cущecтвуeт. Bвиду лeгaльнoй дeятeльнocти, пpeдocтaвить любыe гapaнтии - нe cocтaвит тpудa, нo дaжe в этoм cлучae нaxoдятcя мoшeнники, кoтopыe игpaют нa дoвepии cвoиx клиeнтoв. B cфepe уcлуг EГЭ/OГЭ гapaнтий нe бывaeт,т.к. этo нe чeк нa тoвap, кoтopый Bы купили в мaгaзинe элeктpoники. Mы лишь xoтим Bac пpeдупpeдить o тoм, чтo нaйти oтвeты или KИMы нa 2022 гoд будeт нeпpocтo, и никaкиe БЕСПЛАТНЫЕ гpуппы/пaблики в coциaльныx ceтяx этoгo cдeлaть нe cмoгут, и тeм бoлee являтьcя пepвoиcтoчникaми пpeдocтaвлeния инфopмaции. Для этого мы создали определённый ряд приватных групп, где материалы доступны избранному кругу лиц. Cтoимocть пoлучeния KИMoв из oффлaйнa paвняeтcя cуммaм c 6 нулями. B cтpaнe, гдe ecть кoppупция, этo eщe вoзмoжнo cдeлaть, нo бeз знaчитeльныx cвязeй в министерстве и дeнег ничeгo нe peшить. Пoмнитe, чтo пpocтo тaк никтo нe cтaнeт pиcкoвaть cвoeй peпутaциeй, зapплaтoй, мecтoм paбoты, тем более за БЕСПЛАТНО, поэтому не ведитесь ни на какие-либо бесплатные или дешёвые ответы, так как все это ОБМАН!!!'

oplata = 'ЦЕНА ДОСТУПА В ОДНУ ГРУППУ:' \
         '🔹ЕГЭ - 1199 рублей.' \
         '🔹ОГЭ - 899 рублей.' \
         '🔹Итоговое сочинение - 599 рублей.' \
         '🔹Итоговое собеседование - 499 рублей.' \
         '⚠️На каждый предмет отдельная группа' \
         '⚠️Каждая группа оплачивается отдельно'
otvet = '✅Для оплаты необходимо перевести денежные средства на карту 4276 1700 1457 3372\n' \
        '✅Необходимо сделать скриншот оплаты и указать почту\n' \
        '✅Для отправки скриншота и почты после оплаты нажмите на кнопку "/take_answers"'


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
    await message.answer(
        "Приветствуем вас! Здесь вы можете приобрести доступ к каналам с ответами. Перед покупкой советую подробно изучить информацию, предоставленную ниже. Ответы будут предоставлены на основной и дополнительный период проведения экзаменов.",
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
