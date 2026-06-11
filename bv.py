# =========================================================
# 1. IMPORTS
# =========================================================

import asyncio

from aiogram import Bot, Dispatcher, F

from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    FSInputFile,
    InputMediaPhoto
)

from aiogram.filters import CommandStart


# =========================================================
# 2. BOT TOKEN
# =========================================================

# /* 2.1 */

BOT_TOKEN = "7948226500:AAHLR8NBA_LiKxC_2AKfRmuPfPQ4ao3xx4Q"


# =========================================================
# 3. BOT + DISPATCHER
# =========================================================

# /* 3.1 */
# Создание бота

bot = Bot(token=BOT_TOKEN)

# /* 3.2 */
# Создание диспетчера

dp = Dispatcher()


# =========================================================
# 4. DATABASE (JSON STYLE)
# =========================================================

# /* 4.1 */
# Здесь хранятся все категории,
# описания и фотографии

data = {

    # =====================================================
    # /* 4.1.1 */
    # КАТЕГОРИЯ — СУМКИ
    # =====================================================
    # =====================================================
    # /* 4.1.1 */
    # КАТЕГОРИЯ — СУМКИ
    # =====================================================    

    "bags": {

        # /* 4.1.1.1 */
        # Название категории

        "title": "👜 Сумка-тоут середнього розміру",

        # /* 4.1.1.2 */
        # Описание категории

        "description": " Ділова сумка-тоут середнього розміру від італійського бренду Virginia Conti. Аксесуар виготовлений з якісної натуральної гладкої шкіри глибокого чорного кольору. Сумка має елегантну трапецієподібну форму із витонченими вертикальними металевими вставками сріблястого кольору біля основи ручок. Вона оснащена двома надійними середніми ручками для носіння на лікті чи в руці, довгим регульованим знімним ремінцем на плече та декоративним шкіряним брелоком-тегом. У сумки одне відділення на блискавці, всередині перегородка-кишеня на блискавці, є маленька кишенька на блискавці, дві великі кишені для телефону. Також є невелика кишеня на блискавці на задній стороні сумки. ",

        # /* 4.1.1.3 */
        # Фотографии категории

        "photos": [

            "photos/10001.jpg",
            "photos/10002.jpg",
            "photos/10003.jpg",
            "photos/10004.jpg",
        ]
    },

    # =====================================================
    # /* 4.1.2 */
    # КАТЕГОРИЯ — ОБУВЬ
    # =====================================================

    "shoes": {

        # /* 4.1.2.1 */
        # Название категории

        "title": "👠 Велика жіноча сумка-тоут (шопер) ",

        # /* 4.1.2.2 */
        # Описание категории

        "description": "Стильная обувь сезона",

        # /* 4.1.2.3 */
        # Фотографии категории

        "photos": [

            "photos/bv.jpg",
            "https://drive.google.com/u/0/drive-viewer/AKGpihYFChmEjZm4t4mU7dLhbrZYejHjnToRViWCfLNW2L3Ze3GHmPubEui49XUIXq-PtUpv8780Ih0haWv0l0ge8kmWbPv05HN9NkI=s2560?auditContext=forDisplay"
        ]
    }
}


# =========================================================
# 5. MAIN MENU
# =========================================================

# /* 5.1 */
# Главное меню после /start

main_menu = InlineKeyboardMarkup(

    inline_keyboard=[

        # /* 5.1.1 */
        # 1 строка
        [
            InlineKeyboardButton(text="📚 Ассортимент", callback_data="catalog"),
            InlineKeyboardButton(text="🎥 XXL", callback_data="video")
        ],

        # /* 5.1.2 */
        # 2 строка
        [
            InlineKeyboardButton(text="🧠 Heroes of the Storm", callback_data="tests"),
            InlineKeyboardButton(text="📞 World of Warcraft", callback_data="contacts")
        ],

        # /* 5.1.3 */
        # 3 строка (запас / будущие кнопки)
        [
            InlineKeyboardButton(text="⭐ Discord", callback_data="new"),
            InlineKeyboardButton(text="ssssssssssssssss1sssssss2sss3sss", callback_data="hot")
        ],

        # /* 5.1.4 */
        # 4 строка (ещё место под рост)
        [
            InlineKeyboardButton(text="💬 Поддержка", callback_data="support"),
            InlineKeyboardButton(text="ℹ️ О нас", callback_data="about")
        ]
    ]
)


# =========================================================
# 6. CATALOG MENU
# =========================================================

# /* 6.1 */
# Подменю каталога

catalog_menu = InlineKeyboardMarkup(

    inline_keyboard=[

        # /* 6.1.1 */
        # Кнопка сумки

        [
            InlineKeyboardButton(
                text="👜 Велика жіноча сумка-тоут (шопер) ",
                callback_data="bags"
            )
        ],

        # /* 6.1.2 */
        # Кнопка обувь

        [
            InlineKeyboardButton(
                text="👠 Обувь",
                callback_data="shoes"
            )
        ],

        # /* 6.1.3 */
        # Кнопка назад

        [
            InlineKeyboardButton(
                text="⬅️ Назад",
                callback_data="back_main"
            )
        ]
    ]
)


# =========================================================
# 7. START COMMAND
# =========================================================

# /* 7.1 */
# Срабатывает при /start

@dp.message(CommandStart())
async def start(message: Message):

    # /* 7.1.1 */
    # Стартовая картинка

    photo = FSInputFile("photos/bv.jpg")

    # /* 7.1.2 */
    # Отправка картинки + текста + меню

    await message.answer_photo(

        photo=photo,

        caption="""
Valenti — 07.05.2026 17:36
Я обкурился бля
𝑩𝒊𝒕𝒕𝒆𝒓𝒔𝒘𝒆𝒆𝒕 — 07.05.2026 17:39
молодец
страховка це не покриває
""",

        reply_markup=main_menu
    )


# =========================================================
# 8. OPEN CATALOG
# =========================================================

# /* 8.1 */
# Открытие каталога

@dp.callback_query(F.data == "catalog")
async def open_catalog(callback: CallbackQuery):

    # /* 8.1.1 */
    # Меняем сообщение

    await callback.message.edit_caption(

        caption="""
📚 Каталог

Выберите категорию:
""",

        reply_markup=catalog_menu
    )


# =========================================================
# 9. BACK TO MAIN MENU
# =========================================================

# /* 9.1 */
# Возврат в главное меню

@dp.callback_query(F.data == "back_main")
async def back_main(callback: CallbackQuery):

    # /* 9.1.1 */
    # Меняем сообщение обратно

    await callback.message.edit_caption(

        caption="""
Главное меню 🔥
""",

        reply_markup=main_menu
    )


# =========================================================
# 10. OPEN BAGS CATEGORY
# =========================================================

# /* 10.1 */
# Открытие раздела сумок

@dp.callback_query(F.data == "bags")
async def open_bags(callback: CallbackQuery):

    # /* 10.1.1 */
    # Получаем данные категории

    item = data["bags"]

    # /* 10.1.2 */
    # Создаем массив для media group

    media = []

    # /* 10.1.3 */
    # Перебираем фотографии

    for i, photo_path in enumerate(item["photos"]):

        # /* 10.1.3.1 */
        # Загружаем фото

        photo = FSInputFile(photo_path)

        # /* 10.1.3.2 */
        # Если первое фото —
        # добавляем описание

        if i == 0:

            media.append(

                InputMediaPhoto(
                    media=photo,
                    caption=item["description"]
                )
            )

        # /* 10.1.3.3 */
        # Остальные фото без текста

        else:

            media.append(

                InputMediaPhoto(
                    media=photo
                )
            )

    # /* 10.1.4 */
    # Отправляем media group

    await bot.send_media_group(

        chat_id=callback.message.chat.id,
        media=media
    )

    # /* 10.1.5 */
    # Кнопка назад

    back_menu = InlineKeyboardMarkup(

        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="⬅️ Назад",
                    callback_data="catalog"
                )
            ]
        ]
    )

    # /* 10.1.6 */
    # Отправляем кнопку назад

    await callback.message.answer(

        text="👜 Раздел сумок",

        reply_markup=back_menu
    )


# =========================================================
# 11. OPEN SHOES CATEGORY
# =========================================================

# /* 11.1 */
# Открытие раздела обуви

@dp.callback_query(F.data == "shoes")
async def open_shoes(callback: CallbackQuery):

    # /* 11.1.1 */
    # Получаем данные категории

    item = data["shoes"]

    # /* 11.1.2 */
    # Создаем media group

    media = []

    # /* 11.1.3 */
    # Перебираем фото

    for i, photo_path in enumerate(item["photos"]):

        # /* 11.1.3.1 */
        # Загружаем фото

        photo = FSInputFile(photo_path)

        # /* 11.1.3.2 */
        # Первое фото с описанием

        if i == 0:

            media.append(

                InputMediaPhoto(
                    media=photo,
                    caption=item["description"]
                )
            )

        # /* 11.1.3.3 */
        # Остальные без описания

        else:

            media.append(

                InputMediaPhoto(
                    media=photo
                )
            )

    # /* 11.1.4 */
    # Отправка media group

    await bot.send_media_group(

        chat_id=callback.message.chat.id,
        media=media
    )

    # /* 11.1.5 */
    # Кнопка назад

    back_menu = InlineKeyboardMarkup(

        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="⬅️ Назад",
                    callback_data="catalog"
                )
            ]
        ]
    )

    # /* 11.1.6 */
    # Сообщение после фото

    await callback.message.answer(

        text="👠 Раздел обуви",

        reply_markup=back_menu
    )


# =========================================================
# 12. OTHER BUTTONS
# =========================================================

# /* 12.1 */
# Видео

@dp.callback_query(F.data == "video")
async def video(callback: CallbackQuery):

    await callback.answer("пока тут нихуя нет")


# /* 12.2 */
# Тесты

@dp.callback_query(F.data == "tests")
async def tests(callback: CallbackQuery):

    await callback.answer("и тут нихуя")


# /* 12.3 */
# Контакты

@dp.callback_query(F.data == "contacts")
async def contacts(callback: CallbackQuery):

    await callback.answer("так же нихуя")


# =========================================================
# 13. START BOT
# =========================================================

# /* 13.1 */
# Главная функция запуска

async def main():

    # /* 13.1.1 */
    # Запуск polling

    await dp.start_polling(bot)


# =========================================================
# 14. ENTRY POINT
# =========================================================

# /* 14.1 */
# Точка входа

if __name__ == "__main__":

    asyncio.run(main())
