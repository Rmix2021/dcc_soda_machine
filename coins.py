class Coin:
    def __init__(self, name, value):
        self.value = value
        self.name = name

class Dime:
    def __init__(self):
        super(Dime, self).__init__("Dime", 0.10)

class Nickel:
    def __init__(self):
        super(Nickel, self).__init__("Nickel", 0.05)

class Penny:
    def __init__(self):
        super(Penny, self).__init__("Penny", 0.01)

class Quarter:
    def __init__(self):
        super(Quarter, self).__init__("Quarter", 0.25)
