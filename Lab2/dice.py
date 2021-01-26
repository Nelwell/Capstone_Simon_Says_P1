# Dice example class

import random


class Dice:
    def __init__(self, sides=6):  # can give default value here
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)  # lowest range to highest range, which is number of sides


dice = Dice(6)  # number of sides on dice
for roll in range(100):
    print(dice.roll())

# example with default value of sides given
dice2 = Dice()
print(dice2.roll())