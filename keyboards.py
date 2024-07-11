from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Товары"),
            KeyboardButton(text="Профиль")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

buy_products_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Электронника"),
            KeyboardButton(text="Канцелярия"),
            KeyboardButton(text="Другое"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

buy_electronic_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Флешка"),
            KeyboardButton(text="Мышка"),
            KeyboardButton(text="Наушники"),
            KeyboardButton(text="Повербанк"),
            KeyboardButton(text="Колонка"),
        ],
        [
            KeyboardButton(text="Коврик для мыши")
        ],
        [
            KeyboardButton(text="Кольцо-держатель для селфи")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

buy_kancelariya_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Скетчбук"),
            KeyboardButton(text="Блокнот")
        ],
        [
            KeyboardButton(text="Цветные карандаши")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

buy_other_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Тредники"),
            KeyboardButton(text="Кружка"),
            KeyboardButton(text="Значки"),
            KeyboardButton(text="Жвачка")
        ],
        {
            KeyboardButton(text="Конфеты на палочке")
        }
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

buy_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Купить')
        ],
        [
            KeyboardButton(text='Назад')
        ]
    ],
)
