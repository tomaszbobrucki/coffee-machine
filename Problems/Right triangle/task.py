class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        self.area = 0.5 * leg_1 * leg_2


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
if input_a ** 2 + input_b ** 2 == input_c ** 2:
    tri = RightTriangle(input_c, input_b, input_a)
    print(f'{tri.area:.1f}')
else:
    print("Not right")
