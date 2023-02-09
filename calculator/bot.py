import telebot
import calc

with open('token.txt', 'r', encoding='utf-8') as inf:
    token = str(inf.read())

bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start'])


def handle_text(message):
    mes_1 = bot.send_message(message.chat.id, 'Вас приветствует калькулятор! ')
    mes_4 = bot.send_message(message.chat.id, 'Введите число: ')
    bot.register_next_step_handler(mes_4, input_num_1)

def input_num_1(message):
    global num_1
    num_1 = message.text
    if calc.is_number(num_1):
        mes_2 = bot.send_message(message.chat.id, 'Введите число: ')
        bot.register_next_step_handler(mes_2, input_num_2)
    else:
        bot.send_message(message.chat.id, 'ошибка, введите команду /start')


def input_num_2(message):
    global num_2
    num_2 = message.text
    if calc.is_number(num_2):
        mes_3 = bot.send_message(message.chat.id, 'Введите операцию (+, -, *, /, ^): ')
        bot.register_next_step_handler(mes_3, input_oper)
    else:
        bot.send_message(message.chat.id, 'ошибка, введите команду /start')


def input_oper(message):
    global oper
    oper = message.text
    match oper:
        case '+':
            res = calc.sum(num_1, num_2)
            bot.send_message(message.chat.id, res) 
            bot.send_message(message.chat.id, 'чтобы начать сначала, введите команду /start')   
        case '-':
            res = calc.sub(num_1, num_2)
            bot.send_message(message.chat.id, res)
            bot.send_message(message.chat.id, 'чтобы начать сначала, введите команду /start')    
        case '*':
            res = calc.mult(num_1, num_2)
            bot.send_message(message.chat.id, res)
            bot.send_message(message.chat.id, 'чтобы начать сначала, введите команду /start')    
        case '/':
            res = calc.div(num_1, num_2)
            bot.send_message(message.chat.id, res)
            bot.send_message(message.chat.id, 'чтобы начать сначала, введите команду /start')    
        case '^':
            res = calc.exp(num_1, num_2)
            bot.send_message(message.chat.id, res)
            bot.send_message(message.chat.id, 'чтобы начать сначала, введите команду /start')    
        case _:
            bot.send_message(message.chat.id, 'ошибка, введите команду /start')


