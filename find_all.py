# объявление функции
def find_all(target, symbol):
	symbol_num = []
	for i in range(len(target)):
		if target[i] == symbol:
			symbol_num.append(i)
	return symbol_num

# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))
