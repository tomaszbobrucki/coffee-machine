# put your python code here
new_list = []
while True:
    i = int(input())
    if 10 <= i <= 100:
        new_list.append(i)
    elif i > 100:
        break

for k in new_list:
    print(k)
