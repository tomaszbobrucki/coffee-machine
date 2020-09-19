new_list = []

while True:
    name = input()
    if name == ".":
        break
    new_list.append(name)

print(new_list)
print(len(new_list))
