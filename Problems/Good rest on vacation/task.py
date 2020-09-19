# put your python code here
duration = int(input())
food = int(input())
flight_one_way = int(input())
one_night = int(input())

result = (duration * food
          + flight_one_way * 2
          + one_night * (duration - 1))

print(result)
