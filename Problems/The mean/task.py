mean = 0
counter = 0

while True:
    number = input()
    if number == ".":
        break
    mean += int(number)
    counter += 1

print(mean / counter)
