max1 = 0
shop = []
while True:
    name = input().split()
    if "MEOW" in name:
        break
    elif int(name[1]) >= max1:
        max1 = int(name[1])
        shop = name[0]
print(shop)
