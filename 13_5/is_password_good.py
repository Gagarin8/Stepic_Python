# объявление функции
def is_password_good(password):
    score = 0
    if len(password) >= 8 and password != password.upper() and password != password.lower():
        score += 1
    for c in password:
        if c in '0123456789':
            score += 1
            break
    if score == 2:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
