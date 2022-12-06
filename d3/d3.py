"""
Carson Rohan
AOC2022
Day 3: Binary shakedown
"""

import os

ASCII_A_DEC = 65
ASCII_LOWERCASE_A_DEC = 97
ALPHABET_SIZE = 26
FILE_NAME = 'd3i.txt'

def main():

	# get input from input file
	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), FILE_NAME), 'r') as input:
		packs = input.readlines()

	print(Part1().searchPacks(packs))

	print(Part2().search3Packs(packs))

	return 0


class Part1:
	"""
	Search for a char that appears in both halves of a list
	Use binary search
	"""
	def searchPacks(self, packs: list):
		score: int = 0

		for pack in packs:
			# half len minus newline
			halfSackLen = len(pack[:-1]) // 2
			firstHalf = list(pack[:halfSackLen])
			secondHalf = list(pack[:-1][halfSackLen:])

			firstHalf.sort(key=lambda a: ord(a) % ASCII_LOWERCASE_A_DEC)
			secondHalf.sort(key=lambda a: ord(a) % ASCII_LOWERCASE_A_DEC)

			for item in firstHalf:

				foundChar = self.getItem(item, secondHalf)

				if (foundChar != ''):
					
					# check if A-Z or a-z
					if (ord(foundChar) < ASCII_LOWERCASE_A_DEC):
						score += ord(foundChar) - ASCII_A_DEC + ALPHABET_SIZE +  1
						break
					else:
						score += ord(foundChar) - ASCII_LOWERCASE_A_DEC + 1
						break

		return score

	def getItem(self, targetItem: chr, items: list):
		# items should already be sorted for binary search
		low: int = 0
		high: int = len(items) - 1
		mid: int = 0
		
		# perform binary search
		while (low <= high):
			mid = (high + low) // 2

			if (ord(items[mid]) % ASCII_LOWERCASE_A_DEC < ord(targetItem) % ASCII_LOWERCASE_A_DEC):
				low = mid + 1

			elif (ord(items[mid]) % ASCII_LOWERCASE_A_DEC > ord(targetItem) % ASCII_LOWERCASE_A_DEC):
				high = mid - 1

			else:
				return items[mid]

		return ''

	def sortRule(self, char):
		return ord(char) % ASCII_LOWERCASE_A_DEC

class Part2:
	"""
	This time, search through 3 lists for the same char

	Binary search keeps computation time down, but another trick here
	is to remove duplicates so we aren't searching the same char over and over
	"""
	def search3Packs(self, packs: list):
		score: int = 0

		for i in range(0, len(packs), 3):
			pack1 = list(packs[i][:-1])
			pack2 = list(packs[i + 1][:-1])
			pack3 = list(packs[i + 2][:-1])

			packGroup = pack1 + pack2 + pack3

			# remove duplicates and sort
			packGroup = [*set(packGroup)]
			packGroup.sort(key=Part1().sortRule)
			pack1 = [*set(pack1)]
			pack1.sort(key=Part1().sortRule)
			pack2 = [*set(pack2)]
			pack2.sort(key=Part1().sortRule)
			pack3 = [*set(pack3)]
			pack3.sort(key=Part1().sortRule)

			for item in packGroup:
				result1 = Part1().getItem(item, pack1) 
				result2 = Part1().getItem(item, pack2)
				result3 = Part1().getItem(item, pack3)

				if (result1 != '' and result2 != '' and result3 != ''):

					# check if A-Z or a-z
					if (ord(result1) < ASCII_LOWERCASE_A_DEC):
						score += ord(result1) - ASCII_A_DEC + ALPHABET_SIZE +  1
						break
					else:
						score += ord(result1) - ASCII_LOWERCASE_A_DEC + 1
						break

		return score

if __name__ == '__main__':
	main()