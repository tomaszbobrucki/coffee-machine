x = int(input())
y = int(input())

# if (x == 1 or x == 8) and (y == 1 or y == 8):
if not 1 < x < 8 and not 1 < y < 8:
    print(3)
elif 2 <= x <= 7 and 2 <= y <= 7:
    print(8)
else:
    print(5)
