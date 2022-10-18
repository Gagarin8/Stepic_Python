# объявление функции
def is_magic(date):
    date = [int(i) for i in date.split('.')]
    return date[0] * date[1] == date[2] % 100

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))
