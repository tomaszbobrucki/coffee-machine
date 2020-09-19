class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        self.cents += deposit_cents
        while True:
            if self.cents > 99:
                self.cents -= 100
                self.dollars += 1
            else:
                break


# pig = PiggyBank(1, 1)
# pig.add_money(500, 500)
# print(pig.dollars, pig.cents)
