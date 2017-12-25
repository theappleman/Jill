#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

from pybooru import Danbooru

client = Danbooru('danbooru')

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
configFile = open("config.txt", "r") #Replace that line with YOUR config.txt
token = str(configFile.readline())

def start(bot, update):
    
    update.message.reply_text('Hi {}!'.format(update.message.from_user.first_name))

def help(bot, update):
    
    update.message.reply_text("""
    Jill at your service.

I can't do much for now, but here is what I can do at the moment:

/help, will make me print out the command list(what you are reading right now)

/hello will greet you, because you know, I'm polite.
/porn your_kink, sends 10 pictures from danbooru. let's say, you wanna see pictures of lolis(hello ludo), just type: /porn lolis
""")


def conversation(bot, update):
    
    print("wip")

    ## Make the bot talk, when a non-command message is sent. WIP
def send_picture(bot, update, args):
    query = str(args[0])
    posts = client.post_list(tags=query, limit=20)
    
    for post in posts:
        update.message.reply_text("There you go: https://danbooru.donmai.us{0}".format(post['file_url']))

    

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    updater = Updater(token)

    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("hello", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("porn", send_picture, pass_args=True))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, conversation))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
