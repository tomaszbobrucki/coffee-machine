income = int(input())


def tax(income1, tax1):
    calc_tax = (income1 * tax1) / 100
    print(f'The tax for {income1} is {tax1}%. That is {round(calc_tax)} dollars!')


if income >= 132407:
    tax(income, 28)
elif income >= 42708:
    tax(income, 25)
elif income >= 15528:
    tax(income, 15)
else:
    tax(income, 0)
