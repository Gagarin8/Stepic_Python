# объявление функции
def get_factors(num):
    factors = []
    for i in range (1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))
