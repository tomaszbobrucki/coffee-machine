n = int(input())
numbers = []

for _ in range(n):
    j = int(input())
    if j % 7 == 0:
        numbers.append(j)

for j in numbers:
    print(j ** 2)
