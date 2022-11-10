import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
char = ''

number_of_password = input('Укажите количество требуемых паролей для генерации:')
password_lenght = input('Укажите длину пароля:')
digits_on = input('Включить в пароль цифры 0123456789?(y/n):')
ABC_on = input('Включить в пароль прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?(y/n):')
abc_on = input('Включить в пароль строчные буквы abcdefghijklmnopqrstuvwxyz?(y/n):')
punct_on = input('Включить в пароль символы !#$%&*+-=?@^_?(y/n):')
ambiguous_char = input('Исключить неодночначные символы il1Lo0O?(y/n)')
