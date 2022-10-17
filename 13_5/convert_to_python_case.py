# объявление функции
def convert_to_python_case(text):
    text2 = ''
    for i in range(len(text)):
        if i == 0 and text[i].isupper():
            text2 += text[i].lower()
            continue
        if text[i].isupper():
            text2 += '_' + text[i].lower()
            continue
        text2 += text[i]
    return text2

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
