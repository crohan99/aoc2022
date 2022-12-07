"""
Carson Rohan
AOC2022
Day 4: Name_of_puzzle
"""

import os

FILE_NAME = 'd4i.txt'

def main():

	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), FILE_NAME)) as input:
		fileInput = input.read().splitlines()

	print(Part1.getDupeSectionCount(fileInput))

class Part1:

	def getDupeSectionCount(sections: list):
		sectionRangeElf1: tuple
		sectionRangeElf2: tuple
		dupeSectionsCount: int = 0

		for sectionPair in sections:
			sectionRangeElf1 = (int(sectionPair.split(',')[0].split('-')[0]), int(sectionPair.split(',')[0].split('-')[1]))
			sectionRangeElf2 = (int(sectionPair.split(',')[1].split('-')[0]), int(sectionPair.split(',')[1].split('-')[1]))
			print(sectionRangeElf1)
			print(sectionRangeElf2)
			print('')

			if (Part1.isSubset(range(sectionRangeElf1[0], sectionRangeElf1[1]), range(sectionRangeElf2[0], sectionRangeElf2[1])) |
				Part1.isSubset(range(sectionRangeElf2[0], sectionRangeElf2[1]), range(sectionRangeElf1[0], sectionRangeElf1[1]))):
				print("dupe")
				print('')
				dupeSectionsCount += 1

		return dupeSectionsCount

	def isSubset(range1, range2):
		if (len(range1) == 0):
			return range1.start in range2

		# return true if one of the set's extremes are between the other set's
		return range1.start in range2 and range1[-1] in range2


class Part2:

	def blah():
		return 0

if __name__ == '__main__':
	main()

# 472 too low
# 479 wrong
# 551 too high
# 552 too high