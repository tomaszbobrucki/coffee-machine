# put your python code here
first = float(input())
second = float(input())
operation = input()

if operation in '/, mod, div' and second == 0:
    print("Division by 0!")
elif operation == '+':
    print(first + second)
elif operation == '-':
    print(first - second)
elif operation == '*':
    print(first * second)
elif operation == 'pow':
    print(first ** second)
elif operation == '/':
    print(first / second)
elif operation == 'mod':
    print(first % second)
elif operation == 'div':
    print(first // second)
