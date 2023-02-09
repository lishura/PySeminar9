from logg import logging
from bot import *

def main():
    logging.info('Start program')
    bot.polling()
    logging.info('Session finish')


if __name__ == '__main__':
    main()