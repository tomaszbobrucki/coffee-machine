x = float(input())
y = float(input())
'''
if x > 0 and y > 0:
    print("I")
elif x < 0 and y > 0:
    print("II")
elif x < 0 and y < 0:
    print("III")
elif x > 0 and y < 0:
    print("IV")
'''
if x > 0:
    if y > 0:
        print("I")
    else:
        print("IV")
else:
    if y > 0:
        print("II")
    else:
        print("III")
