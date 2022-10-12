# объявление функции
def number_of_factors(num):
    number = 0
    for i in range (1, num + 1):
        if num % i == 0:
            number += 1
    return number

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))
