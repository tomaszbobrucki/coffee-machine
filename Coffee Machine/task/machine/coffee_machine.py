"""
print("Starting to make a coffee")
print("Grinding coffee beans")
print("Boiling water")
print("Mixing boiled water with crushed coffee beans")
print("Pouring coffee into the cup")
print("Pouring some milk into the cup")
print("Coffee is ready!")

water = int(input("Write how many ml of water the coffee machine has:"))
milk = int(input("Write how many ml of milk the coffee machine has:"))
coffee = int(input("Write how many grams of coffee beans the coffee machine has:"))
cups_number = int(input("Write how many cups of coffee you will need: "))

WATER_ML = 200
MILK_ML = 50
COFFEE_G = 15

def how_many_cups(water1, milk1, coffee1):
    cups1 = min(water1 // WATER_ML, milk1 // MILK_ML, coffee1 // COFFEE_G)
    return cups1

cups = how_many_cups(water, milk, coffee)

if cups == cups_number:
    print("Yes, I can make that amount of coffee")
elif cups > cups_number:
    print("Yes, I can make that amount of coffee (and even {} more than that)".format(cups-cups_number))
else:
    print("No, I can make only {} cups of coffee".format(cups))


print("For", cups_number, "cups of coffee you will need: ")
print(cups_number * WATER_ML, "ml of water")
print(cups_number * MILK_ML, "ml of milk")
print(cups_number * COFFEE_G, "g of coffee beans")
"""
water_all = 400
milk_all = 540
beans_all = 120
cups_all = 9
money_all = 550

#  water, milk, beans, price
espresso = [250, 0, 16, 4]
latte = [350, 75, 20, 7]
cappuccino = [200, 100, 12, 6]


def current_ingredients():
    print("The coffee machine has:")
    print("{} of water".format(water_all))
    print("{} of milk".format(milk_all))
    print("{} of coffee beans".format(beans_all))
    print("{} of disposable cups".format(cups_all))
    print("${} of money".format(money_all))


# def take_action():
# while True:
# action = input("Write action (buy, fill, take, remaining, exit):")
# if action == "buy":
# buy()
# elif action == "fill":
# fill()
# elif action == "take":
# take()
# elif action == "remaining":
# remaining()
# elif action == "exit":
# exit()
def fill():
    global water_all
    global milk_all
    global beans_all
    global cups_all
    global money_all
    water_add = int(input("Write how many ml of water do you want to add:"))
    water_all += water_add
    milk_add = int(input("Write how many ml of milk do you want to add:"))
    milk_all += milk_add
    beans_add = int(input("Write how many grams of coffee beans do you want to add:"))
    beans_all += beans_add
    cups_add = int(input("Write how many disposable cups of coffee do you want to add:"))
    cups_all += cups_add


def take():
    global money_all
    print("I gave you ${}".format(money_all))
    money_all = 0


def remaining():
    current_ingredients()


def buy_coffee(name):
    global water_all
    global milk_all
    global beans_all
    global cups_all
    global money_all

    water_need = water_all // name[0]
    if name[1] == 0:
        milk_need = milk_all
    else:
        milk_need = milk_all // name[1]
    beans_need = beans_all // name[2]

    cups = min(water_need, milk_need, beans_need)
    if cups >= 1:
        print("I have enough resources, making you a coffee!")
        water_all -= name[0]
        milk_all -= name[1]
        beans_all -= name[2]
        cups_all -= 1
        money_all += name[3]
    else:
        if water_need <= milk_need <= beans_need:
            print("Sorry, not enough water!")
        elif milk_need <= water_need <= beans_need:
            print("Sorry, not enough milk!")
        else:
            print("Sorry, not enough beans!")


# def main():
#  current_ingredients()
#  print()
# take_action()
#  print()
#  current_ingredients()

class MachineCoffee:

    def __init__(self):
        self.choose_option()

    def choose_option(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):")
            if action == "buy":
                self.buy()
            elif action == "fill":
                fill()
            elif action == "take":
                take()
            elif action == "remaining":
                remaining()
            elif action == "exit":
                exit()

    def buy(self):
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if choice == "back":
            self.choose_option()
        elif int(choice) == 1:
            buy_coffee(espresso)
        elif int(choice) == 2:
            buy_coffee(latte)
        elif int(choice) == 3:
            buy_coffee(cappuccino)


machine = MachineCoffee()
