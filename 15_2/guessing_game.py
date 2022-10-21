import random


#Выбор случайного числа
def random_number(n):
    return random.randint(1, n)


#Проверка числа
def is_valid(num, up_num):
    return str(num).isdigit() and 1 <= int(num) <= int(up_num)


#Старт игры "Угадайка"
def start_game():    
    print('Добро пожаловать в числовую угадайку')
    print('Мы будем угадывать целое число от 1 до ...(введите верхнее значение диапазона):', end=' ')
    count = 0
    up_num = input()
    while not is_valid(up_num, up_num):
            print('А может быть все-таки введем целое число больше 1?')
            print('Введите верхнее значение диапазона:', end=' ')
            up_num = input()
    n = random_number(int(up_num))
    print('Угадайте целое число от 1 до', up_num, 'включительно, которое задумал компьютер.')
    print('Введите его здесь:', end = ' ')
    while True:        
        digit = input()
        count += 1
        if not is_valid(digit, up_num):
            print('А может быть все-таки введем целое число от 1 до', up_num, '?')
            continue
        if int(digit) < int(n):
            print('Ваше число меньше загаданного, попробуйте еще разок')
            continue
        if int(digit) > int(n):
            print('Ваше число больше загаданного, попробуйте еще разок')
            continue
        if int(digit) == int(n):
            print('Вы угадали за', count, 'попыток, поздравляем!')
            game_again()
            break


#Играть заново
def game_again():
    print('Хотите повторить игру?')
    print('Нажмите "y", если нет - нажмите "n":', end=' ')
    answer = input()
    if answer == 'y':
        start_game()
    elif answer == 'n':
        finish_game()
    else:
        print('Что за кракозябру Вы ввели?')
        game_again()


#завершение игры
def finish_game():
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')


start_game()#Вызов игры
