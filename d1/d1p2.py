import os

"""
Carson Rohan
AOC2022
Day 1 Part 2: Top 3 fat elves
"""

FILE_NAME = r'/d1i1.txt'

def main():

    elfPacks = day1()

    # grab max of list, add to total, then pop it (x3)
    top3: int = 0
    for i in range(3):
        top3 += max(elfPacks)
        elfPacks.remove(max(elfPacks))

    print(top3)

    return 0

def day1():
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

    return elfPacks

if __name__ == "__main__":
    main()