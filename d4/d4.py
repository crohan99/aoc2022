"""
Carson Rohan
AOC2022
Day 4: Name_of_puzzle
"""

import os

# FILE_NAME = 'd4i.txt'
FILE_NAME = 'testinput.txt'

def main():

	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), FILE_NAME)) as input:
		fileInput = input.read().splitlines()

	print(Part1().getDupeSectionCount(fileInput))
	print(Part2().getDupeSectionCount(fileInput))

	return 0

class Part1:

	def getDupeSectionCount(self, sections: list):
		sectionRangeElf1: tuple
		sectionRangeElf2: tuple
		dupeSectionsCount: int = 0

		for sectionPair in sections:
			sectionRangeElf1 = (int(sectionPair.split(',')[0].split('-')[0]), int(sectionPair.split(',')[0].split('-')[1]))
			sectionRangeElf2 = (int(sectionPair.split(',')[1].split('-')[0]), int(sectionPair.split(',')[1].split('-')[1]))

			if (self.isBetween(sectionRangeElf1, sectionRangeElf2) or self.isBetween(sectionRangeElf2, sectionRangeElf1)):
				dupeSectionsCount += 1

		return dupeSectionsCount

	def isBetween(self, set1: tuple, set2: tuple):
		if (len(set1) == 2 and len(set2) == 2):

			if (set1[0] == set1[-1]):
				return set1[0] >= set2[0] and set1[-1] <= set2[-1]

			if (set1[0] >= set2[0] and set1[-1] <= set2[-1]):
				return True

		return False

class Part2:

	def getDupeSectionCount(self, sections: list):
		sectionRangeElf1: list
		sectionRangeElf2: list
		dupeSectionsCount: int = 0

		for sectionPair in sections:
			sectionRangeElf1 = [int(sectionPair.split(',')[0].split('-')[0]), int(sectionPair.split(',')[0].split('-')[1])]
			sectionRangeElf2 = [int(sectionPair.split(',')[1].split('-')[0]), int(sectionPair.split(',')[1].split('-')[1])]

			if (self.hasOverlap(sectionRangeElf1, sectionRangeElf2)):
				dupeSectionsCount += 1

		return dupeSectionsCount

	def hasOverlap(self, set1: list, set2: list):
		totalLen: int = len(set1) + len(set2)
		# return True if the combined lists had duplicates removed
		set1.extend(set2)
		x = set(set1)
		return len(set(set1)) != totalLen

if __name__ == '__main__':
	main()

# 472 too low
# 479 wrong
# 551 too high
# 552 too high