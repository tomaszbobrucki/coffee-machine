scores = input().split()
# put your python code here
win_all, fail_all = 0, 0

for i in scores:
    if i == "C":
        win_all += 1
    elif i == "I":
        fail_all += 1
    if fail_all == 3:
        print("Game over")
        print(win_all)
        break
else:
    print("You won")
    print(win_all)
