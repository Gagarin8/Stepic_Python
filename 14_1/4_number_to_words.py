# объявление функции
def number_to_words(num):
    list_1 = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
    list_11 = ['', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    list_21 = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    if num < 11:
        return list_1[num]
    elif num < 20:
        return list_11[num - 10]
    elif num % 10 == 0:
        return list_21[int(num / 10)]
    else:
        return list_21[num // 10] + ' ' + list_1[num % 10]

# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))