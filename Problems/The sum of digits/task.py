# put your python code here
number = int(input())

a = int(number / 100)
b = int((number - a * 100) / 10)
c = number - a * 100 - b * 10

print(a + b + c)
