import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, point):
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)


#  p1 = Point(1.5, 1)
#  p2 = Point(1.5, 2)

#  print(p1.dist(p2))
