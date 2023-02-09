import telebot
import csv
import os

with open('token.txt', 'r', encoding='utf-8') as inf:
    token = str(inf.read())

bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start'])


def handle_text(message):
    mes_1 = bot.send_message(message.chat.id, 'Вас приветствует телефонный справочник! ')
    mes_2 = bot.send_message(message.chat.id, 'Доступные операции с телефонной книгой:\n\
    1 - печать телефонной книги;\n\
    2 - добавление контакта;\n\
    3 - удаление контакта;\n')
    mes_3 = bot.send_message(message.chat.id, 'Введите номер операции: ')

    bot.register_next_step_handler(mes_3, input_num_oper)

def input_num_oper(message):
    global num_oper
    global phone_number
    num_oper = message.text
    match num_oper:
        case '1':
            bot.send_message(message.chat.id, print_contacts(message)) 
        case '2':
            mes_4 = bot.send_message(message.chat.id, 'Введите Ф.И.О. нового контакта: ')
            bot.register_next_step_handler(mes_4, get_work)                     
        case '3':
            mes_5 = bot.send_message(message.chat.id, "Введите ID контакта для удаления: ")
            bot.register_next_step_handler(mes_5, delete_contact)  
        case _:
            bot.send_message(message.chat.id, 'ошибка, наберите команду start')


def get_work(message):
    global name
    name = message.text
    mes_5 = bot.send_message(message.chat.id, 'Введите должность нового контакта: ')
    bot.register_next_step_handler(mes_5, get_phone_number)
            

def get_phone_number(message):
    global work
    work = message.text
    mes_6 = bot.send_message(message.chat.id, 'Введите номер нового контакта: ')
    bot.register_next_step_handler(mes_6, add_contact)


def add_contact(message):
    global phone_number
    phone_number = message.text
    with open('last_ID.txt', 'r', encoding='utf-8') as info:
        last_ID = int(info.read())
    with open('contacts.csv', 'a', encoding='utf-8') as file:
        columns = ["ID", "Ф.И.О.", "Должность", "Телефон"]
        file_writer = csv.DictWriter(file, delimiter = ",", lineterminator="\r", fieldnames=columns)
        file_writer.writerow({"ID": last_ID+1, "Ф.И.О.": name, "Должность": work, "Телефон": phone_number})
    with open('last_ID.txt','w', encoding='utf-8') as f:
        f.write(str(last_ID+1))
    bot.send_message(message.chat.id, f"В телефонную книгу добавлен контакт с ID {last_ID+1}. Для вызова меню наберите команду start")
        

def print_contacts(message):
    with open('contacts.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)  
        line_count = 0   
        for row in csv_reader:
            if line_count == 0:
                header = str("                   ".join(row))
                bot.send_message(message.chat.id, header)
                line_count+=1
            result = str(f'{row["ID"].center(5)} {row["Ф.И.О."].center(40)} {row["Должность"].center(20)} {row["Телефон"].center(15)}')
            bot.send_message(message.chat.id, result)
            line_count+=1
    bot.send_message(message.chat.id, 'Для вызова меню наберите команду start')


def delete_contact(message):
    global id_del
    id_del = int(message.text)
    with open('contacts.csv', 'r', encoding='utf-8') as inp, open('contacts_del.csv', 'w', encoding='utf-8', newline='') as out:
        columns = ["ID", "Ф.И.О.", "Должность", "Телефон"]
        csv_reader = csv.DictReader(inp)
        csv_writer = csv.DictWriter(out, fieldnames=columns)
        csv_writer.writeheader()
        line_count = 0 
        for row in csv_reader:
            if int(row["ID"]) != id_del:
                csv_writer.writerow({"ID": line_count+1, "Ф.И.О.": row["Ф.И.О."], "Должность": row["Должность"], "Телефон": row["Телефон"]})
                line_count+=1
    with open('last_ID.txt','w', encoding='utf-8') as f:
        f.write(str(line_count))
    os.remove('contacts.csv')
    os.rename('contacts_del.csv', 'contacts.csv')
    bot.send_message(message.chat.id, f"Контакт с ID {id_del} удален из телефонной книги. Для вызова меню наберите команду start")
    


bot.polling(none_stop=True)



    
