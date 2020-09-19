initial = int(input())
final = int(input())
days = 0

while final < initial:
    initial = initial / 2
    days += 12

print(days)
