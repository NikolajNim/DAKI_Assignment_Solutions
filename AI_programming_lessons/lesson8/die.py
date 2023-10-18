import random
class Die:

    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        print(random.randint(1, self.sides))
