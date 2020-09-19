user = int(input())
maximum = int(input())

total = (user / maximum) * 100

if total < 60:
    print("F")
elif 60 <= total < 70:
    print("D")
elif 70 <= total < 80:
    print("C")
elif 80 <= total < 90:
    print("B")
else:
    print("A")
