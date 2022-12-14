import os

"""
Carson Rohan
AOC2022
Day 1 Part 1: Fat elves
"""

FILE_NAME = r'/d1i1.txt'

def main():

    # get input from input file
    with open(os.path.dirname(os.path.abspath(__file__)) + FILE_NAME, 'r') as input:
        snackList = input.readlines()

    elfPacks: list = []
    calorieAmount: int = 0
    calorieTotal: int = 0

    for snack in snackList:
        # strip newline
        calorieAmount = snack[:-1]

        # if there is a number after taking away newline, add that number to total
        if (len(calorieAmount) > 0):
            calorieTotal += int(calorieAmount)

        # we encountered the end of an elf's pack. Take the total and add to that elf's data and
        # reset the counter
        else:
            elfPacks.append(calorieTotal)
            calorieTotal = 0

    print(max(elfPacks))
    return 0

if __name__ == "__main__":
    main()