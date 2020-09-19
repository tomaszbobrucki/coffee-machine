class Stack:

    def __init__(self):
        self.new = []

    def push(self, el):
        self.new.append(el)

    def pop(self):
        return self.new.pop()

    def peek(self):
        return self.new[-1]

    def is_empty(self):
        return self.new == []


# tomek = []
# lala = Stack(tomek)
# lala.push("t")
# print(tomek)
# print(lala.is_empty())
