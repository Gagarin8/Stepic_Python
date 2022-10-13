# объявление функции
def is_palindrome(text):
    text_list = list()
    text = text.lower()
    for c in text:
        if c.isalpha():
            text_list.append(c)
    return text_list == text_list[::-1]



# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
