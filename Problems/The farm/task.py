money = int(input())

if money < 23:
    print("None")
elif 23 <= money < 678:
    print(str(money // 23) + " chickens" if money // 23 > 1 else "1 chicken")
elif 678 <= money < 1296:
    print(str(money // 678) + " goats" if money // 678 > 1 else "1 goat")
elif 1296 <= money < 3848:
    print(str(money // 1296) + " pigs" if money // 1296 > 1 else "1 pig")
elif 3848 <= money < 6769:
    print(str(money // 3848) + " cows" if money // 3848 > 1 else "1 cow")
else:
    print(money // 6769, "sheep")
