field = [str(x) for x in range(1, 10)]


def draw_field():
    print('-'*20)
    for i in range(3):
        for j in range(3):
            print(f'{field[j+i*3]:^5}', end=' ')
        print(f"\n{'-'*20}")
    print()


def motion(sign):
    global field
    while True:
        answer = input(f'Введите число от 1 до 9.\nВыберите позицию {sign}? ')
        if answer.isdigit() and int(answer) in range(1, 10):
            answer = int(answer)
            position = field[answer-1]
            if position != chr(10060) and position != chr(11093):
                if sign == 'x':
                    field[answer-1] = chr(10060)
                elif sign == '0':
                    field[answer-1] = chr(11093)
                break


def win():
    win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8))
    n = [field[x[0]]
         for x in win_combinations if field[x[0]] == field[x[1]] == field[x[2]]]
    return n[0] if n else n


def play():
    counter = 0
    draw_field()
    while True:
        motion('0') if counter % 2 else motion('x')
        draw_field()
        if counter > 3:
            if win():
                print(f'{win()} - выйграл!')
                break
        if counter == 8:
            print(f'Ничья')
            break
        counter += 1


play()
