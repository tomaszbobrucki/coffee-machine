A = int(input())
B = int(input())
H = int(input())

if H > B:
    print("Excess")
else:
    if H < A:
        print("Deficiency")
    else:
        print("Normal")
