class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(self):
        print(f'Hello, I am {self.name}!')


me = Person(input())
me.greet()
