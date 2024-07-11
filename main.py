import asyncio
import keyboards
from bot_token import token
from aiogram import Bot, Dispatcher, F, types
from aiogram.types import Message

bot = Bot(token())
dp = Dispatcher()


@dp.message(F.text == "/start")
async def start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}. Это онлаин-магазин Codologia.\nПанель управления находится внизу ↓ ",
                         reply_markup=keyboards.main_kb)


@dp.message(F.text.lower() == "профиль")
async def profile(message: Message):
    await message.answer(f'Ваш профиль:'
                         f'\nИмя: {message.from_user.first_name}'
                         f'\nФамилия (если указана): {message.from_user.last_name}'
                         f'\nID Профиля: {message.from_user.id}'
                         f'\nПроверка на бота: {message.from_user.is_bot}')


@dp.message(F.text.lower() == "товары")
async def cotigories(message: types.Message):
    await message.answer(f"Выберите категорию",
                         reply_markup=keyboards.buy_products_kb)


@dp.message(F.text.lower() == "электронника")
async def buy_flashdrive(message: types.Message):
    await message.answer(f"Выберите товар",
                         reply_markup=keyboards.buy_electronic_kb)


@dp.message(F.text.lower() == "канцелярия")
async def buy_flashdrive(message: types.Message):
    await message.answer(f"Выберите товар",
                         reply_markup=keyboards.buy_kancelariya_kb)


@dp.message(F.text.lower() == "другое")
async def buy_flashdrive(message: types.Message):
    await message.answer(f"Выберите товар",
                         reply_markup=keyboards.buy_other_kb)


@dp.message(F.text.lower() == "флешка")
async def buy_flashdrive(message: Message):
    await message.answer(f'\nНазвание: Флешка'
                         f'\nОписание: Флешка от компании Chigmasters, размером 16 гб. Они шедевро маленькая и вы можете носить её с свеём рукзаке'
                         f'\nСтоимость: 28 кодоинов', reply_markup=keyboards.buy_kb)


@dp.message(F.text.lower() == "мышка")
async def buy_mouse(message: Message):
    await message.answer(f'\nНазвание: Мышка'
                         f'\nОписание: Мышка ультра супер про макс 3000 900. Та самая что ломается при любом касании. DPI - 0.006, иммено о такой мышке вы думайте когда видите что ваш тимейт в кс ходит только в вперёд и назад'
                         f'\nСтоимость: 55 кодокоинов',
                         reply_markup=keyboards.buy_kb)


@dp.message(F.text.lower() == "коврик для мыши")
async def buy_mouse_pad(message: Message):
    await message.answer(f'\nНазвание: Коврик для мыши'
                         f'\nОписание: Ткань? Бумага? Неееет. Пластик. Легенда своего времени (нашего или не нашего). С этим ковриком ваша мышка (да и вышка) полетит как по льду, за что вас сразу же забанит VAC в кс'
                         f'\nСтоимость: 45 кодокоинов',
                         reply_markup=keyboards.buy_kb)


@dp.message(F.text.lower() == "наушники")
async def buy_headphones(message: Message):
    await message.answer(f'\nНазвание: Наушники'
                         f'\nОписание: Беспроводные между прочим. Для настоящих меломанов есть и ультра про супер-лайт макс супер ульта шелли'
                         f'\nСтоимость: 65 кодокоинов',
                         reply_markup=keyboards.buy_kb)


@dp.message(F.text.lower() == "повербанк")
async def buy_power_bank(message: Message):
    await message.answer(f'\nНазвание: Повербанк'
                         f'\nОписание: Повербанк на 1 вольт. Заряжается быстро, и разряжается тоже быстро'
                         f'\nСтоимость: 66 кодокоинов',
                         reply_markup=keyboards.buy_kb)


@dp.message(F.text.lower() == "колонка")
async def buy_column(message: Message):
    await message.answer(f'\nНазвание: Колонка'
                         f'\nОписание: Тоже для любитилей музыки, главное не забыть выключить блютус перед прослушиванием голосовых сообщений'
                         f'\nСтоимость: 65 кодокоинов',
                         reply_markup=keyboards.buy_kb)


@dp.message(F.text.lower() == "кольцо-держатель для селфи")
async def buy_selfie_ring(message: Message):
    await message.answer(f'\nНазвание: Кольцо-держатель для селфи'
                         f'\nОписание: Без понятия что это вообще. Нахрен оно вообще здесь существует?'
                         f'\nСтоимость: 57 кодокоинов',
                         reply_markup=keyboards.buy_kb)


@dp.message(F.text.lower() == "скетчбук")
async def buy_sketchbook(message: Message):
    await message.answer(f'\nНазвание: Скетчбук'
                         f'\nОписание: Английсикие эти ваши слова, нифига не понятно'
                         f'\nСтоимость: 30 кодокоинов',
                         reply_markup=keyboards.buy_kb)


@dp.message(F.text.lower() == "блокнот")
async def buy_notebook(message: Message):
    await message.answer(f'\nНазвание: Блокнот'
                         f'\nОписание: Воооо, вот это понято. Намного лучше скетчбука какого так как тот совсем уже бука'
                         f'\nСтоимость: 20 кодокоинов',
                         reply_markup=keyboards.buy_kb)


@dp.message(F.text.lower() == "цветные карандаши")
async def buy_colour_pencils(message: Message):
    await message.answer(f'\nНазвание: Цветные карандаши'
                         f'\nОписание: '
                         f'\nСтоимость: 25 кодокоинов',
                         reply_markup=keyboards.buy_kb)


@dp.message(F.text.lower() == "тредники")
async def buy_(message: Message):
    await message.answer(f'\nНазвание: Тредники'
                         f'\nОписание: А? Что? Каво? Трудится чтоли? Я не хочу трудится'
                         f'\nСтоимость: 16 кодокоинов',
                         reply_markup=keyboards.buy_kb)


@dp.message(F.text.lower() == "кружка")
async def buy_mug(message: Message):
    await message.answer(f'\nНазвание: Кружка'
                         f'\nОписание: Вот это реальная вещь. Для настоящих любитилей чая'
                         f'\nСтоимость: 35 кодокоинов',
                         reply_markup=keyboards.buy_kb)


@dp.message(F.text.lower() == "значки")
async def buy_badge(message: Message):
    await message.answer(f'\nНазвание: Значки'
                         f'\nОписание: Типо такие маленькие, которые ещё на ткань можно цеплять'
                         f'\nСтоимость: 16 кодокоинов',
                         reply_markup=keyboards.buy_kb)


@dp.message(F.text.lower() == "жвачка")
async def buy_bubble_gum(message: Message):
    await message.answer(f'\nНазвание: Жвачка'
                         f'\nОписание: Та самая за 1 рубль?'
                         f'\nСтоимость: 9 кодокоинов',
                         reply_markup=keyboards.buy_kb)


@dp.message(F.text.lower() == "конфеты на палочке")
async def buy_lollipops(message: Message):
    await message.answer(f'\nНазвание: Конфеты на палочке'
                         f'\nОписание: Конфеты, палочка в подарок'
                         f'\nСтоимость: 9 кодокоинов',
                         reply_markup=keyboards.buy_kb)


@dp.message(F.text.lower() == "назад")
async def comback_catigories(message: Message):
    await message.answer(f"Выберите категорию",
                         reply_markup=keyboards.buy_products_kb)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
