# put your python code here
a = int(input())
b = int(input())
counter, sum_i = 0, 0


for i in range(a, b + 1):
    if i % 3 == 0:
        sum_i += i
        counter += 1

print(sum_i / counter)
