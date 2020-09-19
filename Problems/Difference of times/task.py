# put your python code here
hours_1 = int(input())
minutes_1 = int(input())
seconds_1 = int(input())
hours_2 = int(input())
minutes_2 = int(input())
seconds_2 = int(input())
result = (seconds_2 - seconds_1
          + (minutes_2 - minutes_1) * 60
          + (hours_2 - hours_1) * 60 ** 2)
print(result)
