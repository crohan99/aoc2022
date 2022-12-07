"""
Carson Rohan
AOC2022
Day 5: LIFO-Fun
"""

import os
import queue

FILE_NAME = 'd5i.txt'
# FILE_NAME = 'testinput.txt'

def main():

	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), FILE_NAME)) as input:
		fileInput = input.readlines()

		Part1().moveCrates(fileInput)

		return 0

class Part1:

	numStacks: int = 0
	highestStackHeight: int = 0
	stacks: dict = {}
	procedures: dict = {}


	def moveCrates(self, input: list):
		print(self.prepInput(input))
		cratesDict = self.prepInput(input)

		return 0

	def moveCrate(self):
		return 0

	def prepInput(self, lines: list):
		procedureIdx: int = 0
		procedureNum: int = 0

		for i in range(len(lines)):

			if (lines[i] == '\n'):
				# get total number of stacks by grabbing the last number in the stack enumeration
				self.numStacks = int(''.join(lines[i - 1].split())[-1])
				# highest stack height is the number of lines it took to get to the number enumeration
				self.highestStackHeight = (i + 1) - 2
				# instructions start here
				procedureIdx = i

			# store instructions
			if (procedureIdx != 0):
				procedureNum += 1
				# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
				# figure out how to store procedure
				self.procedures[procedureNum] = lines[i]


		for j in range(self.highestStackHeight - 1, -1, -1):
			stackLine: str = lines[j]
			stackNum: int = 1

			while (len(stackLine) != 0):
				# check for [
				# if yes, then grab the letter inside and put it into a list of lists
				# if no [ then remove a tab width and repeat
				print(stackLine[0])

				if (stackLine[0] == '['):

					if (stackNum in self.stacks.keys()):
						self.stacks[stackNum].append(stackLine[1])
					else:
						self.stacks[stackNum] = [stackLine[1]]

					# 4 is the space a [#] takes + 1 space
					stackLine = stackLine[4:]
					print(stackLine)
				else:
					stackLine = stackLine.lstrip()
					print(stackLine)

				stackNum += 1

		print(self.stacks)
		return self.stacks

class Part2:

	def blah():
		return 0

if __name__ == '__main__':
	main()

