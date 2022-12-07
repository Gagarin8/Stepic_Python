import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
char = ''

number_of_password = int(input('Укажите количество требуемых паролей для генерации:'))
password_lenght = int(input('Укажите длину пароля:'))
digits_on = input('Включить в пароль цифры 0123456789?(y/n):')
ABC_on = input('Включить в пароль прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?(y/n):')
abc_on = input('Включить в пароль строчные буквы abcdefghijklmnopqrstuvwxyz?(y/n):')
punct_on = input('Включить в пароль символы !#$%&*+-=?@^_?(y/n):')
ambiguous_char = input('Исключить неодночначные символы il1Lo0O?(y/n):')

if digits_on.lower() == 'y':
    char += digits
if ABC_on.lower() == 'y':
    char += uppercase_letters
if abc_on.lower() == 'y':
    char += lowercase_letters
if punct_on.lower() == 'y':
    char += punctuation
if ambiguous_char.lower() == 'y':
    for c in 'il1Lo0O':
        char = char.replace(c, '')


def generate_password(password_lenght, char):
    password = ''
    for j in range(password_lenght):
        password += random.choice(char)
    return password


for _ in range(number_of_password):
    print(generate_password(password_lenght, char))
