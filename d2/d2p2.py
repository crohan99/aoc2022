"""
Carson Rohan
AOC2022
Day 2 Part 2: Rock, paper, scissors, lizard, Spock, modulo
"""

import d2p1 as d

def getTotalScore(rounds: list):
	totalScore: int = 0

	for round in rounds:
		choices = round[:-1].split(' ')
		totalScore += getRoundScore(choices[0], choices[1])

	return totalScore

def getRoundScore(opponentChoice: chr, myChoice: chr):
	# do this the dumb way first
	# if 1 then choose (mine-other)%3 == 2 (lose)
	# if (ord(myChoice) - d.ASCII_X_VALUE == 1):

	# if 2 then choose (mine-other)%3 == 0 (draw)

	# if 3 then choose (mine-other)%3 == 1 (win)

	return 0

if __name__ == '__main__':
	getTotalScore()