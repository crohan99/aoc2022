"""
Carson Rohan
AOC2022
Name_of_puzzle
"""

import os

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
	# choices are ABC -> 123 or XYZ -> 123
	# difference of choices % 3 gives us [0: draw, 1: myChoice wins, 2: opponentChoice wins]
	# score multiplier is just 3 so add 1 to this ^ and modulo by multiplier, then multipy by multiplier
	# finish by adding choice value
	return ((((((ord(myChoice) - ASCII_X_VALUE) + 1) - ((ord(opponentChoice) - ASCII_A_VALUE) + 1)) % NUM_VARIABLES) + 1) % NUM_OUTCOMES) * NUM_OUTCOMES + ((ord(myChoice) - ASCII_X_VALUE) + 1)

if __name__ == '__main__':
	getTotalScore()