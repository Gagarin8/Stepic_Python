# объявление функции
def draw_triangle(x, y):
    for i in range(y):
        print(' ' * (x // 2 - i) + '*' * (i + 1) + '*' * i)

# основная программа
a, b = 15, 8
draw_triangle(a, b)  # вызов функции
