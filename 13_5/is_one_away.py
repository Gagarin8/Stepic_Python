# объявление функции
def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False
    else:
        score = len(word1)
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                score -= 1
        return score == 1

# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))
