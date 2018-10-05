from http_parser import get_rating
from liker import make_magic_like

available_filters = ['all', 'top']


def get_stat(bot, update, args):
    bot.send_message(chat_id=update.message.chat_id, text='Подожди, интернет плохой....')
    response_text = ''

    if args:
        if args[-1] not in available_filters:
            if args[-1].isdigit() and args[-2] == 'top':
                response_text = get_rating(f_name=args[-2], f_count=int(args[-1]))
            else:
                response_text = f'Не известное значение фильтра {args[-2]}. Должна быть цифра'
        else:
            response_text = f'Не известный фильтр {args[-1]}. Доступоные фильтры {available_filters}'

    bot.send_message(chat_id=update.message.chat_id, text=response_text or get_rating())

    if response_text == '':
        bot.send_message(chat_id=update.message.chat_id, text='Тут нет пользователей которые набрали менее 2-х лайков')


def set_like(bot, update, args):
    bot.send_message(chat_id=update.message.chat_id, text='Это займет некоторое время. Ожидай...')

    if len(args) > 1 and args[0].isdigit() and args[1].isdigit():
        response_text = make_magic_like(int(args[0]), int(args[1]))
        response_text = (
            f'Вот эти пользователи поставили лайки:\n{response_text}'
            '\n'
            'Введи /stat для просмотра результатов'
        )
    else:
        response_text = (
            'Нужно указать id пользователя и количество лайков через пробел. Например:\n'
            '<команда> <id> <количество лайков>\n'
            '/like 37 20000'
        )

    bot.send_message(chat_id=update.message.chat_id, text=response_text)


def help_resp(bot, update):
    text = (
        'Доступные команты:\n'
        '/start - лучше не вводить\n'
        '\n'
        '/help - эта справка'
        '\n'
        '/stat - статистика по пользователям\n'
        '/stat all - все пользователи\n'
        '/stat top 3 - первые 3 пользователя в рейтинге]\n'
        '\n'
        '/like 37 2000 - поставить 2000 лайков пользователю 37\n'
    )
    bot.send_message(chat_id=update.message.chat_id, text=text)


def start(bot, update):
    text = (
        'Пошёл на хуй!\n'
        'Или введи /help :)'
    )
    bot.send_message(chat_id=update.message.chat_id, text=text)
