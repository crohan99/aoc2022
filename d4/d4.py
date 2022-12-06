"""
Carson Rohan
AOC2022
Day 4: Name_of_puzzle
"""

import os

FILE_NAME = 'testinput.txt'

def main():

	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), FILE_NAME)) as input:
		fileInput = input.read().splitlines()

	print(Part1.getNumDuplicateSections(fileInput))

class Part1:

	def getNumDuplicateSections(sections: list):
		sectionRangeElf1: tuple
		sectionRangeElf2: tuple

		for sectionPair in sections:
			sectionRangeElf1 = (sectionPair.split(',')[0].split('-')[0], sectionPair.split(',')[0].split('-')[1])
			sectionRangeElf2 = (sectionPair.split(',')[1].split('-')[0], sectionPair.split(',')[1].split('-')[1])
			print(sectionPair.split(',')[1][:-1].split('-')[1])
			print(sectionRangeElf1)
			print(sectionRangeElf2)

		return 0

	def rangeIsSubset(range1, range2):

		if not range1:
			return True
		if not range2:
			return False
		if (len(range1) > 1 and range1.step % range2.step):
			return False

		return range1.start in range2 and range1[-1] in range2


class Part2:

	def blah():
		return 0

if __name__ == '__main__':
	main()