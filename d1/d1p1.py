import os
import sys

def main():

    # get input from input file
    with open(os.path.dirname(os.path.abspath(__file__)) + r'/d1i1.txt', 'r') as input:
        calorie_list = input.readlines()
        print(calorie_list)

    return 0

if __name__ == "__main__":
    main()