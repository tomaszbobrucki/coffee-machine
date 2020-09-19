# our class Ship
class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    # the old sail method that you need to rewrite
    def sail(self, destination):
        return "The {} has sailed for {}!".format(self.name, destination)


black_pearl = Ship("Black Pearl", 800)
destination1 = input()
print(black_pearl.sail(destination1))
