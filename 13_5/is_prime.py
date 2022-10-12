# объявление функции
def is_prime(num):
    score = 0
    for i in range(2, num):
        if num % i == 0 and num != 2:
            score += 1
    if score > 0 or num == 1:
        return False
    else:
        return True

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))
