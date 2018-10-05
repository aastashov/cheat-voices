#!/usr/bin/env python
from telegram.ext import CommandHandler, Updater

from settings import TELEGRAM_TOKEN
from t_bot import get_stat, start, help_resp, set_like

if __name__ == '__main__':
    updater = Updater(token=TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    register_handlers = (
        ('start', start),
        ('stat', get_stat, dict(pass_args=True)),
        ('help', help_resp),
        ('like', set_like, dict(pass_args=True)),
    )

    for handler in register_handlers:
        start_handler = CommandHandler(handler[0], handler[1], **(handler[2] if len(handler) > 2 else {}))
        dispatcher.add_handler(start_handler)

    updater.start_polling()
