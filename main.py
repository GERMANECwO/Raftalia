import telebot
from telebot import types
from info import (Raftalia, diary, story_good_end, story_underground, story_neutral_end_21111, story_neutral_end_21112,
                  story_bad_end_path211121, story_good_end_path2, story_path2111)

TOKEN = '6436229396:AAETecZbrkuiv_-vWuAlPdnXsl09Xhv_Cxc'
bot = telebot.TeleBot(TOKEN)

# дополнительно
Raftalia_health = 100


@bot.message_handler(commands=["start"])
def start_(message):
    bot.send_message(message.chat.id, f"Запуск успешен!\n{message.from_user.first_name}, Приветствую! Я квест-бот!\n"
                                      f"/help - для информации!")


@bot.message_handler(commands=["help"])
def help_answer(message):
    bot.send_message(message.chat.id, f"Я квест-бот. на данный я могу предложить только 1 квест\n"
                                      f"мои правила вполне просты, много не тыкаем.\nЕсли вылезает ошибка, пишем мне "
                                      f"- \n/links - ссылки куда можно писать мне, чтобы сообщить об ошибке,\n"
                                      f"...или просто сказать спасибо\n"
                                      f"Чтобы начать - /start_game")


@bot.message_handler(commands=["links"])
def handle_links(message):
    bot.reply_to(message, "вот мои ссылки для связи:\n"
                          "ВК - https://vk.com/fxsstd\n"
                          "Тelegram - https://t.me/AlexLse\n")


# начало квеста
@bot.message_handler(commands=['start_game'])
def start_game(message):
    markup_question = types.InlineKeyboardMarkup()
    answer1 = types.InlineKeyboardButton('ДА!', callback_data='Yes')
    answer2 = types.InlineKeyboardButton('Нет', callback_data='No')
    markup_question.add(answer1, answer2)
    bot.send_message(message.chat.id, "Вы готовы начать квест?", reply_markup=markup_question)


# считывание ответа на вопрос да/нет
@bot.callback_query_handler(func=lambda call: True)
def handle_start_game(call):
    # начало квеста с выводом кнопок
    if call.data == 'Yes':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        photo_url = 'https://imgur.com/a/HLuXyha'
        caption = f"Небольшая предыстория.\n    \n" + Raftalia[0] + "\n\nСделайте свой выбор.\n" \
                                                                    "1. Вы можете ворваться в эту давно заброшенную хижину\n" \
                                                                    "2. Разведать вокруг неё, и заглянуть в окна\n" \
                                                                    "3. Не испытывать судьбы и пройти мимо\n" \
                                                                    "Что нужно сделать...? "
        markup = types.InlineKeyboardMarkup()
        itembtn1 = types.InlineKeyboardButton('Ворваться с эффектом неожиданности', callback_data='path1')
        itembtn2 = types.InlineKeyboardButton('Действовать с осторожностью', callback_data='path2')
        itembtn3 = types.InlineKeyboardButton('Не стоит тревожить тех, кто находится в ней..', callback_data='path3')
        markup.add(itembtn1)
        markup.add(itembtn2)
        markup.add(itembtn3)
        bot.send_photo(call.message.chat.id, photo=photo_url, caption=caption, reply_markup=markup,
                       parse_mode="Markdown")

    # отмена начала квеста
    elif call.data == 'No':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Если захотите пройти, то напишите снова /start_game !")

    global Raftalia_health
    # 3 основных выбора

    # путь 1
    if call.data == "path1":
        Raftalia_health -= 25

        markup = types.InlineKeyboardMarkup()
        itembtn1 = types.InlineKeyboardButton('Использовать заклинание "Вспышка"', callback_data='path1_1')
        itembtn2 = types.InlineKeyboardButton('Удар катаной - лунное сияние', callback_data='path1_2')
        markup.add(itembtn1)
        markup.add(itembtn2)
        media = types.InputMediaPhoto(media="https://imgur.com/MIOAc4F",
                                      caption="~Будем действовать шумно!\nПосле того как дверь выбивается,"
                                              " слышен жесткий удар, это был удар магии!\n"
                                              "Потеряно 25 хп.\n В темноте вы видите только ярко белые глаза"
                                              ", которые направляются к вам снова!\n\n Нужно атаковать! Но как?")
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media,
                               reply_markup=markup)

    # путь 2
    elif call.data == "path2":
        markup = types.InlineKeyboardMarkup()
        itembtn1 = types.InlineKeyboardButton('Напасть на духа, используя "Вспышку"', callback_data='path2_1')
        itembtn2 = types.InlineKeyboardButton('Обойти дом вокруг', callback_data='path2_2')
        markup.add(itembtn1)
        markup.add(itembtn2)
        media = types.InputMediaPhoto(media="https://imgur.com/hE53boq",
                                      caption="~Осторожность не повредит.. Вы обходите дом вокруг.\nЗаглядывая в окно, "
                                              "вы видите черное облако, которое летает по всей комнате.."
                                              " Он держится подальше от света окон.. Мне кажется это можно"
                                              " использовать для своего преимущества..\n\nЧто будете"
                                              " делать?\nИспользовать заклинание чтобы осветить всю комнату\nМожет есть"
                                              " другой путь? ")
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media,
                               reply_markup=markup)
    # путь 3
    elif call.data == "path3":
        markup = types.InlineKeyboardMarkup()
        itembtn1 = types.InlineKeyboardButton('Пора возвращаться домой...', callback_data='path3_1')
        markup.add(itembtn1)
        media = types.InputMediaPhoto(media="https://imgur.com/a/Jbr2Wsq",
                                      caption="Лучше я не буду тревожить хозяинов..."
                                              " - сказала Рафталия и развернувшись,"
                                              " начинает уходить от этой хижины")
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media,
                               reply_markup=markup)
# выборы из путей

    # путь 1
    # использование магии
    elif call.data == "path1_1":
        markup = types.InlineKeyboardMarkup()
        itembtn1 = types.InlineKeyboardButton('Войти в дверь', callback_data='path1_1_1')
        itembtn2 = types.InlineKeyboardButton('Лучше осмотреться здесь', callback_data='path1_1_2')
        markup.add(itembtn1)
        markup.add(itembtn2)
        media = types.InputMediaPhoto(media="https://imgur.com/KlqMIek",
                                      caption="Вы произносите заклинание\nПосле этого из ваших рук появляется ярко "
                                              "светящийся шар, который освещает всю комнату. Вы видите призрака, он"
                                              " престает как черное облако, которое растворяется в белом свете"
                                              " и пропадает..\nВы смотрите что есть вокруг и у вас есть выбор\n\n"
                                              "Войти в следующую дверь\nОсмотреть данную комнату")
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media,
                               reply_markup=markup)
    # неудачное нападение, -50хп
    elif call.data == "path1_2":
        Raftalia_health -= 50
        markup = types.InlineKeyboardMarkup()
        itembtn1 = types.InlineKeyboardButton('Использовать заклинание "Вспышка"', callback_data='path1_1')
        itembtn2 = types.InlineKeyboardButton('Попробовать зажечь лампу', callback_data='path1_2_2')
        markup.add(itembtn1)
        markup.add(itembtn2)
        media = types.InputMediaPhoto(media="https://imgur.com/MIOAc4F",
                                      caption="Катана проходит сквозь него. Призрак пролетает через Вас нанося удар!\n"
                                              "Следующего удара вы можете уже не пережить...\nНе зря комната настолько"
                                              " темная.. может, он боится света?")
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media,
                               reply_markup=markup)
    # проигрыш после неуд нападения
    elif call.data == "path1_2_2":
        media = types.InputMediaPhoto(media="https://imgur.com/FIliaom", caption="Вы пытаетесь найти лампу, чтобы "
                                                                                 "осветить комнату. Но тут так темно, "
                                                                                 "что без лампы нельзя найти лампу.\n"
                                                                                 "Вы слышите тишину...\n\n Это конец")
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media)
    # следующая дверь, без бумаг
    elif call.data == "path1_1_1":
        markup = types.InlineKeyboardMarkup()
        itembtn1 = types.InlineKeyboardButton('Я не собираюсь с тобой играть!', callback_data='path1_1_1_1')
        markup.add(itembtn1)
        media = types.InputMediaPhoto(media="https://imgur.com/QpQmYNC",
                                      caption="Вы входите в дверь. Свет от вспышки освещает стол, на котором горят пару"
                                              " свечей. За столом сидит кто-то и начинает говорить, очень старым,"
                                              " хриплым голосом:\nПотерялась девочка? Давай сыграем с тобой в игру...\n"
                                              "Назови мое имя и тогда останешься жива...\n\nВот же ?;*!.."
                                              "Откуда мне знать? Подумала Рафталия про себя..")
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media,
                               reply_markup=markup)
    # проверка, не был ли получен урон в прошлый раз
    elif call.data == "path1_1_1_1":
        if Raftalia_health == 25:

            media = types.InputMediaPhoto(media="https://imgur.com/qHYCxME",
                                          caption="После того как вы это произносите, силуэт замолкает."
                                                  " Дальше вам удается только увидеть горящим красным цветом глаз,"
                                                  " как всё резко пропало.\n\n Вы были сильно потрепанны, вам стоит"
                                                  " отдохнуть..\n\nЭто конец.")
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media)
            return Raftalia_health
        # выдержать удар
        else:
            markup = types.InlineKeyboardMarkup()
            itembtn1 = types.InlineKeyboardButton('Линия тумана', callback_data='path1_1_1_1_1')
            itembtn2 = types.InlineKeyboardButton('Водяной вихрь', callback_data='path1_1_1_1_2')
            markup.add(itembtn1)
            markup.add(itembtn2)
            media = types.InputMediaPhoto(media="https://imgur.com/vjzERh9",
                                          caption="После того как вы это произносите, силуэт замолкает.\nДальше "
                                                  "вам удается только увидеть горящим красным цветом глаз.. Как вдруг"
                                                  " вы видите огромный огненный шар! Вы в последний момент"
                                                  ' уворачиваетесь!\n"А ты шустрая!" - говорит силует..\n\nПора'
                                                  " заканчивать с ним.\nНе хотите ли показать этому силуету свою"
                                                  ' силу?\n1.Ударить лучшим навыком катаной\n2.Использовать магию')
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media,
                                   reply_markup=markup)
    # магия, проигрыш
    elif call.data == "path1_1_1_1_2":
        media = types.InputMediaPhoto(media="https://imgur.com/qHYCxME",
                                      caption="Используя вихрь, ваших сил остается мало.. Вихрь поднимается в комнате, "
                                              "уничтожая мебель и разбрасывая листы бумаги...\nНо вдруг вы видите силует"
                                              " в нем. Ещё мгновенье и он уже перед вами. Пустота..\nИ конец. ")
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media)
    # удар катаной, нейтральная концовка
    elif call.data == "path1_1_1_1_1":
        media = types.InputMediaPhoto(media="https://imgur.com/a/g0nK17S",
                                      caption="Вы начинаете движение в сторону"
                                              " силуета.\nМгновение. Линия тумана!\n\nВзмах! И вы стоите сзади него.\n"
                                              "Ничего не произошло? - спрашивает у себя силует.\n"
                                              "До тех пор, пока стоишь на месте - отвечает Рафталия.\nВы движетесь к"
                                              " выходу, проходя рядом с силуетом он пытается до вас достать, но"
                                              " только начав движение, от него остается только одна половина.\n\n"
                                              "Нейтральная концовка. Вы не нашли ответов, но остались живы.")
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media)
    # осмотр комнаты, нахождение бумаг
    elif call.data == "path1_1_2":
        markup = types.InlineKeyboardMarkup()
        itembtn1 = types.InlineKeyboardButton('Идол Рабьер II!', callback_data='path1_1_1_2')
        markup.add(itembtn1)
        media = types.InputMediaPhoto(media="https://imgur.com/QpQmYNC",
                                      caption=diary[0])
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media,
                               reply_markup=markup)
    # выбор между прощением и отомщением
    elif call.data == "path1_1_1_2":
        markup = types.InlineKeyboardMarkup()
        itembtn1 = types.InlineKeyboardButton('Пощада', callback_data='path1_1_1_2_1')
        itembtn2 = types.InlineKeyboardButton('Убить его', callback_data='path1_1_1_2_2')
        markup.add(itembtn1)
        markup.add(itembtn2)
        media = types.InputMediaPhoto(media="https://imgur.com/pKc2yhG",
                                      caption=story_good_end[0])
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media,
                               reply_markup=markup)
    # прощение, хорошая концовка
    elif call.data == "path1_1_1_2_1":
        media = types.InputMediaPhoto(media="https://imgur.com/EEUA3xn",
                                      caption="'Каждый пожинает то, что посеял. Насилие порождает насилие, и за "
                                              "смерть платят смертью. Те, кто не испытывает сомнений и не знает"
                                              " раскаяния, никогда не вырвутся из этого круга..'\nВы спускаетесь в"
                                              " подвал и видите детей. Они все рады видеть своего"
                                              " спасителя. Вы выходите из этого места. И возвращаетесь в свою деревню"
                                              "\n\nЭто хорошая концовка. Одна из двух")
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media)

    # не прощать.
    elif call.data == "path1_1_1_2_2":
        media = types.InputMediaPhoto(media="https://imgur.com/iQsuta5",
                                      caption="'Ты не имеешь права жить на этом свете!' - говорит Рафталия в ярости.\n"
                                              "Слышен характерный звук удара. Тело бездыханно падает со стула. Но "
                                              "вместо облегчения, вы ощущаете лишь пустоту и утрату."
                                              "\nВы спускаетесь в подвал и видите детей, которые взволнованно бегут к "
                                              "вам. Они все рады видеть своего спасителя!\n"
                                              "Вы выходите из этого места, но сердце наполняется тяжестью и "
                                              "сожалением. Ваша душа не находит покоя, зная, что использовала "
                                              "насилие, даже если это было в защите.\n"
                                              "Нельзя сказать, что это хороший конец... Мир остался ослепленным"
                                              " несправедливостью, которую вы совершили."
                                              "\n\nДля этой концовки есть цитата: 'Око за око - и мир ослепнет..'")
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media)

# путь 2
    # найти другой путь
    elif call.data == "path2_2":
        markup = types.InlineKeyboardMarkup()
        itembtn1 = types.InlineKeyboardButton('Войти в странную дверь', callback_data='path2_2_1')
        itembtn2 = types.InlineKeyboardButton('Вернуться и напасть на монстра', callback_data='path2_1')
        markup.add(itembtn1)
        markup.add(itembtn2)
        media = types.InputMediaPhoto(media="https://imgur.com/pu73HME",
                                      caption="Вы осторожно обходите весь дом, и заходите на задний двор. Очень странно"
                                              ", вы видите открытую дверь, которая ведёт под дом. Вам кажется, не лучшая"
                                              " идея в неё заходить. Из неё идет чувство страха.. Чувство безысходности."
                                              "\n\nЧто будете делать?\nНе смотря ни на что войдете в дверь\n"
                                              "Лучший вариант будет войти через главную дверь..")
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media,
                               reply_markup=markup)
    # проигрыш, закрытие двери
    elif call.data == "path2_2_1":
        media = types.InputMediaPhoto(media="https://imgur.com/0t0AibC",
                                      caption="~Стоит попробовать...\nВы заходите в дверь и спускаетесь всё ниже.. "
                                              "Создается чувство что эта тьма поглощает вас всё больше и больше..\n"
                                              "Вы натыкаетесь на какую-то стенку. И вдруг свет который идёт от двери"
                                              " резко пропадает. Вы остались наедине с темнотой.. Или..?\n\n"
                                              "Глухой удар прерывает вашу идилию с темнотой... И никто больше не видел"
                                              " Рафталию...\nКонец.")
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media)

    # нападение на монстра
    elif call.data == "path2_1":
        markup = types.InlineKeyboardMarkup()
        itembtn1 = types.InlineKeyboardButton('Пойти в подвал', callback_data='path2_1_1')
        itembtn2 = types.InlineKeyboardButton('Войти в дверь', callback_data='path2_1_2')
        markup.add(itembtn1)
        markup.add(itembtn2)
        media = types.InputMediaPhoto(media="https://imgur.com/MUK5aC5",
                                      caption="*Вы врываетесь в дверь*\nДух был готов и нападает, но вы знали что он "
                                              "здесь. Уворачиваетесь от его удара и используете 'Вспышку'. Призрак "
                                              "изчезает в этом белом свете, освещающим всю комнату.\nВам стали"
                                              " быть видны две двери.. Одна, явно ведёт в подвал, другая же в какую то"
                                              " комнату.\n\nЧто будете делать?")
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media,
                               reply_markup=markup)
    # войти в дверь перед подвалом
    elif call.data == "path2_1_2":
        markup = types.InlineKeyboardMarkup()
        itembtn1 = types.InlineKeyboardButton('Пойти в подвал', callback_data='path2_1_1')
        markup.add(itembtn1)
        media = types.InputMediaPhoto(media="https://imgur.com/e1XMduK",
                                      caption="Вы открываете дверь, будучи готовым к нападению, как вдруг это"
                                              " оказывается обычный шкаф... Но осмотревшись в нём вы видите эту.. "
                                              "странную картинку..\n\n~Что она должна значить?")
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media,
                               reply_markup=markup)
    # войти в подвал
    elif call.data == "path2_1_1":
        markup = types.InlineKeyboardMarkup()
        itembtn1 = types.InlineKeyboardButton('Войти в дверь', callback_data='path2_1_1_1')
        itembtn2 = types.InlineKeyboardButton('Открыть клетки', callback_data='path2_1_2_2')
        markup.add(itembtn1)
        markup.add(itembtn2)
        media = types.InputMediaPhoto(media="https://imgur.com/1e3ZOWc",
                                      caption=story_underground[0])
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media,
                               reply_markup=markup)
    # большой выбор, войти в дверь/спасти детей
    # войти в дверь впереди, в подвале
    elif call.data == "path2_1_1_1":
        markup = types.InlineKeyboardMarkup()
        itembtn1 = types.InlineKeyboardButton('Убить силует', callback_data='path2_1_1_1_1')
        itembtn2 = types.InlineKeyboardButton('Уничтожить тотем', callback_data='path2_1_1_1_2')
        markup.add(itembtn1)
        markup.add(itembtn2)
        media = types.InputMediaPhoto(media="https://imgur.com/nhUjRpl",
                                      caption=story_path2111[0])
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media,
                               reply_markup=markup)
    # нападение и убийство силуета, с выводом детей, концовка нейтральная
    elif call.data == "path2_1_1_1_1":
        media = types.InputMediaPhoto(media="https://imgur.com/rywiAWY",
                                      caption=story_neutral_end_21111[0])
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media)
    # послушать ребенка
    elif call.data == "path2_1_1_1_2":
        markup = types.InlineKeyboardMarkup()
        itembtn1 = types.InlineKeyboardButton('Убить силуэт', callback_data='path2_1_1_1_2_1')
        itembtn2 = types.InlineKeyboardButton('Пощадить силует.',
                                              callback_data='path2_1_1_1_2_2')
        markup.add(itembtn1)
        markup.add(itembtn2)
        media = types.InputMediaPhoto(media="https://imgur.com/8uWieLC",
                                      caption=story_neutral_end_21112[0])
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media,
                               reply_markup=markup)
    # убить силует
    elif call.data == "path2_1_1_1_2_1":
        media = types.InputMediaPhoto(media="https://imgur.com/YFhZg5k",
                                      caption=story_bad_end_path211121[0])
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media)
    # пощадить силует
    elif call.data == "path2_1_1_1_2_2":
        media = types.InputMediaPhoto(media="https://imgur.com/wvOEDB6",
                                      caption=story_good_end_path2[0])
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media)

    # спасти детей
    elif call.data == "path2_1_2_2":
        markup = types.InlineKeyboardMarkup()
        itembtn1 = types.InlineKeyboardButton('Спрятаться', callback_data='path2_1_2_2_1')
        itembtn2 = types.InlineKeyboardButton('Напасть, используя заклинание', callback_data='path2_1_2_2_2')
        markup.add(itembtn1)
        markup.add(itembtn2)
        media = types.InputMediaPhoto(media="https://imgur.com/IgGINab",
                                      caption="Вы начинаете открывать клетки..\nДети радостно вас вспоминают."
                                              "Однако, когда вы уже открыли половину клеток, дверь подвала внезапно "
                                              "открывается с громким щелчком. Из коридора доносятся шаги, и вы "
                                              "понимаете, что кто-то или что-то приближается.\n\n У вас "
                                              "возникает выбор:\n\nСпрятаться в тени и надеяться, что незнакомец пройдет "
                                              "мимо..\nили..\nИспользовать заклинание вспышка и напасть на этого незнакомца")
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media,
                               reply_markup=markup)
    # спрятаться
    elif call.data == "path2_1_2_2_1":
        markup = types.InlineKeyboardMarkup()
        itembtn1 = types.InlineKeyboardButton('Войти за силуетом', callback_data='path2_1_2_2_1_1')
        itembtn2 = types.InlineKeyboardButton('Спасти детей', callback_data='path2_1_2_2_1_2')
        markup.add(itembtn1)
        markup.add(itembtn2)
        media = types.InputMediaPhoto(media="https://imgur.com/tKa2n0d",
                                      caption="Вы возвращаете детей в клетки и закрываете их.. А сами прячетесь за "
                                              "коробками.\nЧёрный силуэт проходит мимо и заходит в дверь..\nГромкий "
                                              "хлопок закрытия двери.\n\nТеперь у вас есть выбор:\nВойти за силуэтом "
                                              "в дверь и напасть на него или..\nВывести детей, пока силуэт не заметил.")
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media,
                               reply_markup=markup)
    # спасти детей
    elif call.data == "path2_1_2_2_1_2":
        media = types.InputMediaPhoto(media="https://imgur.com/rywiAWY",
                                      caption="Вы проверяете действительно ли ушёл силуэт.. Выходите из своего"
                                              " укрытия и тихо открываете клетки, выводите детей. Действуя "
                                              "максимально осторожно, вам удается выйти и при этом спасти всех детей!"
                                              "\n\nВы возвращаетесь в деревню..\n\nНейтральная концовка.\nДети спасены,"
                                              " но вы не нашли ответов.")
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media)
    # войти в дверь за силуетом
    elif call.data == "path2_1_2_2_1_1":
        markup = types.InlineKeyboardMarkup()
        itembtn1 = types.InlineKeyboardButton('Катана: Линия тумана', callback_data='path2_1_2_2_1_1_1')
        itembtn2 = types.InlineKeyboardButton('Магия: Вихрь', callback_data='path2_1_2_2_1_2_2')
        markup.add(itembtn1)
        markup.add(itembtn2)
        media = types.InputMediaPhoto(media="https://imgur.com/maaZpZJ",
                                      caption="Вы осторожно выходите из своего укрытия и направляетесь к двери.."
                                              "\n\n~Пора заканчивать! - кричит Рафталия и врывается в комнату."
                                              " Вы видите как привязанное дитё лежит на столе для принесения в жертву."
                                              "\n\nВашего появления никто не ожидал, но силуэт явно остановился и"
                                              " обернувшись бросает в вас ледяные кинжалы.\n\nВы уворачиваетесь.\n"
                                              "Теперь ваша очередь атаковать, только как?\n\n1. Навыком своего вассальн"
                                              "ого оружия\n2. Использовать магию")
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media,
                               reply_markup=markup)
    # лучший навык
    elif call.data == "path2_1_2_2_1_1_1":
        media = types.InputMediaPhoto(media="https://imgur.com/8vBskD9",
                                      caption="Вы начинаете движение в сторону"
                                              " силуета.\nМгновение. Линия тумана!\n\nВзмах! И вы стоите сзади него.\n"
                                              "Ничего не произошло? - спрашивает у себя силует.\n"
                                              "До тех пор, пока стоишь на месте - отвечает Рафталия.\nВы движетесь к"
                                              " выходу, проходя рядом с силуетом он пытается до вас достать, но"
                                              " только начав движение, от него остается только одна половина.\n\n"
                                              "Вы спасаете детей и возвращаетесь в деревню..\n\nНейтральная концовка.\n"
                                              " Вы не нашли ответов, но остались живы.")
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media)
    # использовании магии + инфа о гг
    elif call.data == "path2_1_2_2_1_2_2":
        markup = types.InlineKeyboardMarkup()
        itembtn1 = types.InlineKeyboardButton('Пора заканчивать.. Линия тумана', callback_data='path2_1_2_2_1_1_1')
        markup.add(itembtn1)
        media = types.InputMediaPhoto(media="https://imgur.com/qHYCxME",
                                      caption="Вы произносите заклинание и вихрь поднимается в комнате.\n"
                                              "Всё разлетается по ...\nНо вдруг вы видите силует"
                                              " в нем. Ещё мгновенье и он уже перед вами..\n\n~Только мечь героя щита "
                                              "так хорошо сражается.. Рафталия... Сейчас всё решится, ты или я..\nНЕ "
                                              "ЖДИ ПОЩАДЫ!\nОн наносит вам урон, но"
                                              " вы ещё на ногах и готовы контратаковать!")
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media,
                               reply_markup=markup)
    # использовать вспышку
    elif call.data == "path2_1_2_2_2":
        markup = types.InlineKeyboardMarkup()
        itembtn1 = types.InlineKeyboardButton('Катана: Линия тумана', callback_data='path2_1_2_2_2_1')
        itembtn2 = types.InlineKeyboardButton('Магия: Вихрь', callback_data='path2_1_2_2_2_2')
        markup.add(itembtn1)
        markup.add(itembtn2)
        media = types.InputMediaPhoto(media="https://imgur.com/dmTLUZj",
                                      caption="Слышны громкие и ровные шаги. Как только он проходит рядом с вами\n"
                                              "~Вспышка! - кричит Рафталия. Пояляется из рук белый шар, который вылетая"
                                              " освещает всю комнату. Силуэт пытается закрыться от яркого света, но "
                                              "превосходство на вашей стороне и вы готовы атаковать!\n\nЧто сделаете?"
                                              "\n\n1. Навыком своего вассального оружия\n2. Использовать магию")
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media,
                               reply_markup=markup)
    # лучший навык
    elif call.data == "path2_1_2_2_2_1":
        media = types.InputMediaPhoto(media="https://imgur.com/8vBskD9",
                                      caption="Вы начинаете движение в сторону"
                                              " силуета.\nМгновение. Линия тумана!\n\nВзмах! И вы стоите сзади него.\n"
                                              "Ничего не произошло? - спрашивает у себя силует.\n"
                                              "До тех пор, пока стоишь на месте - отвечает Рафталия.\nВы движетесь к"
                                              " выходу, проходя рядом с силуетом он пытается до вас достать, но"
                                              " только начав движение, от него остается только одна половина.\n\n"
                                              "Вы спасаете детей и возвращаетесь в деревню..\n\nНейтральная концовка.\n"
                                              " Вы не нашли ответов, но остались живы.")
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media)
    # использовать магию
    elif call.data == "path2_1_2_2_2_2":
        media = types.InputMediaPhoto(media="https://imgur.com/fQey3bG",
                                      caption="Используя вихрь, вы замечаете, что силуэт со вспышкой света начинает "
                                              "пропадать.. После того как вихрь прошёл, ничего не осталось от него"
                                              " и вы со спешкой начали спасать детей, чтобы силуэт не вернулся."
                                              "\n\nВы спасаете детей и возвращаетесь в деревню..\n\nНейтральная концовка.\n"
                                              " Вы не нашли ответов, но остались живы.")
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media)
# путь 3
    # путь 3 - нейтральная   концовка
    elif call.data == "path3_1":
        media = types.InputMediaPhoto(media="https://imgur.com/a/6IWg6e2", caption="Может это судьба "
                                                                                   "оберегла меня от опасности "
                                                                                   "внутри?\nДумала Рафталия,"
                                                                                   " будучи в безопасности... живой и здоровой.\n"
                                                                                   "Спасибо за прохождение! Концовка - нейтральная.\nВы не нашли ответов,"
                                                                                   " но остались живы..")
        bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id, media=media)


bot.polling()
