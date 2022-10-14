# объявление функции
def is_valid_password(password):
    score = 0
    for i in range(len(password)): #проверяем на отсутствие третьего двоеточия
        if password[i] == ':':
            score += 1
            if score == 3:
                return False
    for i in range(len(password)): #первая часть пароля
        if password[i] == ':':
            a = password[:i]
            break
    for i in range(len(a) + 1, len(password)): #вторая и третья часть
        if password[i] == ':':
            b = password[len(a) + 1:i]
            c = password[i + 1:]
            break
    b = int(b)
    for i in range(2, b // 2 + 1): #проверяем вторую часть пароля
        if b % i == 0:
            return False
    return a == a[::-1] and int(c) % 2 == 0 #первую и третью


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
