"""
Carson Rohan
AOC2022
Day 5: LIFO-Fun
"""

import os

FILE_NAME = 'd5i.txt'
# FILE_NAME = 'testinput.txt'

def main():

	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), FILE_NAME)) as input:
		fileInput = input.readlines()

		print(Part1().moveCrates(fileInput))
		# print(Part2().moveCrates(fileInput))

		return 0

class Part1:

	def moveCrates(self, input: list):
		"""
		stacks will look like:
		{1: ['A', 'B', 'C'],...}
		procedures will look like:
		{1: ['1', '2, '3'],...}
		"""
		stacks: dict = self.getStacks(input)
		procedures: dict = self.getProcedures(input)

		for proc in procedures.values():
			
			# move crates one at a time
			for i in range(int(proc[0])):
				stacks[int(proc[2])].append(stacks[int(proc[1])].pop())

		topCrates: list = []
		for stack in stacks.values():
			topCrates.append(stack[-1])

		return ''.join(topCrates)

	def getStacks(self, lines: list):
		stacks: dict = {}
		highestStack: int = 0

		for i in range(len(lines)):

			if (lines[i] == '\n'):
				# get total number of stacks by grabbing the last number in the stack enumeration
				# self.numStacks = int(''.join(lines[i - 1].split())[-1])
				# highest stack height is the number of lines it took to get to the number enumeration
				highestStack = (i + 1) - 2
				break

		# store stacks into individual key value pairs
		for j in range(highestStack - 1, -1, -1):
			stackLine: str = lines[j]
			stackNum: int = 1

			while (len(stackLine.strip()) != 0):
				# check for [
				# if yes, then grab the letter inside and put it into a list of lists
				# if no [ then remove a tab width and repeat
				if (stackLine[0] == '['):
					if (stackNum in stacks.keys()):
						stacks[stackNum].append(stackLine[1])
					else:
						stacks[stackNum] = [stackLine[1]]

				# 4 is the space a [#] takes + 
				stackLine = stackLine[4:]
				stackNum += 1

		return stacks

	def getProcedures(self, lines: list):
		procedures: dict = {}
		procedureStart: bool = False
		procedureNum: int = 0

		for i in range(len(lines)):

			# skip everything before single newline
			if (lines[i] == '\n'):
				procedureStart = True
				continue

			# store instructions
			if (procedureStart):
				procedureNum += 1
				procedure = lines[i]

				# store 'move # from # to #' as [#,#,#]
				# ignore how bad this is
				procedures[procedureNum] = [procedure[len('move '):procedure.index('f') - 1], procedure[procedure.index('f') + len('from') + 1:procedure.index('f') + len('from') + 2], procedure[procedure.index('t') + len('to') + 1:procedure.index('t') + len('to') + 3][:-1]]

		return procedures

class Part2:

	def moveCrates(self, input: list):
		"""
		stacks will look like:
		{1: ['A', 'B', 'C'],...}
		procedures will look like:
		{1: ['1', '2, '3'],...}
		"""
		stacks: dict = self.getStacks(input)
		procedures: dict = self.getProcedures(input)

		for proc in procedures.values():

			# add end slice of size proc[0] to stack proc[2] from proc[1]
			stacks[int(proc[2])].append(stacks[int(proc[1])][:(-1 * int(proc[0]))])

			for i in range(int(proc[0])):
				stacks[int(proc[1])].pop()

		topCrates: list = []
		for stack in stacks.values():
			topCrates.append(stack[-1])

		return ''.join(topCrates)

	def pickupCrates():
		return 0

	def getStacks(self, lines: list):
		stacks: dict = {}
		highestStack: int = 0

		for i in range(len(lines)):

			if (lines[i] == '\n'):
				# get total number of stacks by grabbing the last number in the stack enumeration
				# self.numStacks = int(''.join(lines[i - 1].split())[-1])
				# highest stack height is the number of lines it took to get to the number enumeration
				highestStack = (i + 1) - 2
				break

		# store stacks into individual key value pairs
		for j in range(highestStack - 1, -1, -1):
			stackLine: str = lines[j]
			stackNum: int = 1

			while (len(stackLine.strip()) != 0):
				# check for [
				# if yes, then grab the letter inside and put it into a list of lists
				# if no [ then remove a tab width and repeat
				if (stackLine[0] == '['):
					if (stackNum in stacks.keys()):
						stacks[stackNum].append(stackLine[1])
					else:
						stacks[stackNum] = [stackLine[1]]

				# 4 is the space a [#] takes + 
				stackLine = stackLine[4:]
				stackNum += 1

		return stacks

	def getProcedures(self, lines: list):
		procedures: dict = {}
		procedureStart: bool = False
		procedureNum: int = 0

		for i in range(len(lines)):

			# skip everything before single newline
			if (lines[i] == '\n'):
				procedureStart = True
				continue

			# store instructions
			if (procedureStart):
				procedureNum += 1
				procedure = lines[i]

				# store 'move # from # to #' as [#,#,#]
				# ignore how bad this is
				procedures[procedureNum] = [procedure[len('move '):procedure.index('f') - 1], procedure[procedure.index('f') + len('from') + 1:procedure.index('f') + len('from') + 2], procedure[procedure.index('t') + len('to') + 1:procedure.index('t') + len('to') + 3][:-1]]

		return procedures

if __name__ == '__main__':
	main()

