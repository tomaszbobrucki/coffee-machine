min1 = float(input())

while True:
    j = input()
    if j == ".":
        break
    if float(j) < float(min1):
        min1 = j

print(min1)
