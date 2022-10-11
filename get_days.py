# объявление функции
def get_days(month):
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	return days[month -1]

# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))
