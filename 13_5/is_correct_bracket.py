# объявление функции
def is_correct_bracket(text):
    score = 1
    for i in range(len(text)):
        if text[i] == '(':
            score -= 1 
        elif text[i] == ')':
            score += 1 
        if score > 1:
            return False
    return score == 1

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
