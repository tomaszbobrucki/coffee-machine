# put your python code here
sum_all = 0
sum_squares = 0

while True:
    i = int(input())
    sum_all += i
    sum_squares += i ** 2
    if sum_all == 0:
        break

print(sum_squares)
