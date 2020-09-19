# put your python code here
class_1 = int(input())
class_2 = int(input())
class_3 = int(input())

if class_1 % 2 == 0:
    desk_1 = (class_1 // 2)
else:
    desk_1 = (class_1 // 2) + 1

if class_2 % 2 == 0:
    desk_2 = (class_2 // 2)
else:
    desk_2 = (class_2 // 2) + 1

if class_3 % 2 == 0:
    desk_3 = (class_3 // 2)
else:
    desk_3 = (class_3 // 2) + 1

print(desk_1 + desk_2 + desk_3)
