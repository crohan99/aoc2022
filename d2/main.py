"""
Carson Rohan
AOC2022
Main
"""

import os
import d2p1
import d2p2

FILE_NAME = 'd2i.txt'

def main():

	# get input from input file
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), FILE_NAME), 'r') as input:
		rounds = input.readlines()

	print(f'Day 1: {d2p1.getTotalScore(rounds)}')

	print(f'Day 2: {d2p2.getTotalScore(rounds)}')

	return 0

if __name__ == '__main__':
	main()