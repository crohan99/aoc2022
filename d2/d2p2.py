"""
Carson Rohan
AOC2022
Day 2 Part 2: Rock, paper, scissors, lizard, Spock, modulo
"""

NUM_VARIABLES = 3
NUM_OUTCOMES = NUM_VARIABLES
ASCII_A_VALUE = 65
ASCII_X_VALUE = 88

def getTotalScore(rounds: list):
	totalScore: int = 0

	for round in rounds:
		choices = round[:-1].split(' ')
		totalScore += getRoundScore(choices[0], choices[1])

	return totalScore

def getRoundScore(opponentChoice: chr, myChoice: chr):
	# do this in the dumbest way possible because I'm tired
	score: int = 0
	win: int = 1
	lose: int = 2
	draw: int = 0
	winScore: int = 6
	drawScore: int = 3

	# we need to lose (lame)
	if (myChoice == 'X'):

		# cycle through options 0-2
		for i in range(3):
			
			# test 'X', 'Y', and 'Z'
			if (calculateChoice(opponentChoice, chr(ASCII_X_VALUE + i)) == lose):
				score = i + 1
				break

	# we need to draw
	if (myChoice == 'Y'):

		# cycle through options 0-2
		for i in range(3):
			
			# test 'X', 'Y', and 'Z'
			if (calculateChoice(opponentChoice, chr(ASCII_X_VALUE + i)) == draw):
				score = i + 1 + drawScore
				break

	# we need to win (nice)
	if (myChoice == 'Z'):

		# cycle through options 0-2
		for i in range(3):
			
			# test 'X', 'Y', and 'Z'
			if (calculateChoice(opponentChoice, chr(ASCII_X_VALUE + i)) == win):
				score = i + 1 + winScore
				break

	return score

def calculateChoice(choice1: chr, choice2: chr):
	# difference of choices % 3 gives us [0: draw, 1: choice2 wins, 2: choice1 wins]
	return ((((ord(choice2) - ASCII_X_VALUE) + 1) - ((ord(choice1) - ASCII_A_VALUE) + 1)) % NUM_VARIABLES)