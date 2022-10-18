# объявление функции
def is_pangram(text):
    text = text.lower()
    for c in "abcdefghijklmnopqrstuvwxyz":
        if c not in text:
            return False
    return True

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))
