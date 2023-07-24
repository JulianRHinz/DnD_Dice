"""
DnD Dice Roll Generator
"""

# Dice Roll Generator for Dnd, roll 1 or 2 dice with either
# d4,d6,d8,d10,d12,d20 type dice

import os
import random


# Number of Dice
def num_dice():
    while True:
        try:
            num_die = input("How many dice? / Wie viele Würfel? (max 2): ")
            valid_response = "1" "2" "one" "two" "One" "Two" "eins" "zwei" "Eins" "Zwei"
            # accepts both english and german input
            if num_die not in valid_response:
                raise ValueError("1 or 2 only! / Nur 1 oder 2")
            else:
                return num_die
        except ValueError as err:
            print(err)


# Type of Dice

def type_dice():
    while True:
        try:
            type_die = input("Which type of dice? / Welche art von Würfel?")
            valid_response = "d4" "d6" "d8" "d10" "d12" "d20"
            if type_die not in valid_response:
                raise ValueError("Only DnD tye dice! / Nur Dnd Würfel! '\n'd4,d6,d8,d10,d12,d20")
            else:
                return type_die
        except ValueError as err:
            print(err)


# Roll dice

def roll_dice():
    min_value = 1
    max_value = []
    roll_again = "y"

    while roll_again.lower() == "yes" or roll_again.lower() == "y":
        os.system("cls" if os.name == "nt" else "clear")  # Check if windows or linux and clear consul if rolled again
        amount = num_dice()
        dice = type_dice()

        if dice == "d4":
            max_value = 4
        elif dice == "d6":
            max_value = 6
        elif dice == "d8":
            max_value = 8
        elif dice == "d10":
            max_value = 10
        elif dice == "d12":
            max_value = 12
        elif dice == "d20":
            max_value = 20

        if amount == "2" or amount == "two" or amount == "Zwei" or amount == "zwei":
            print("Rolling the dice... / Würfel werden gewürfelt...")
            dice_1 = random.randint(min_value, max_value)
            dice_2 = random.randint(min_value, max_value)

            print("The Values are: / Die Würfel sind gefallen:")
            print("Dice 1 / Würfel 1: ", dice_1)
            print("Dice 2 / Würfel 1: ", dice_2)
            print("Total Value: / Gesamtwert:", dice_1 + dice_2)

            roll_again = input("Roll again? / Nochmal würfel?")

        else:
            print("Rolling the dice... / Würfel werden gewürfelt...")
            dice_1 = random.randint(min_value, max_value)

            print("The Values are: / Die Würfel sind gefallen:")
            print("Dice 1 / Würfel 1: ", dice_1)

            roll_again = input("Roll again? / Nochmal würfel?")


if __name__ == "__main__":
    roll_dice()
