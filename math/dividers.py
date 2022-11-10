n = int(input())
num = []
for i in range(1, (n // 2) + 1):
    if n % i == 0:
        num.append(i)
num.append(n)
print(*num)
