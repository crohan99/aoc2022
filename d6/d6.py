"""
Carson Rohan
AOC2022
Day 6: Swimmin' in the DataStream
"""

import os

FILE_NAME = 'd6i.txt'
# FILE_NAME = 'testinput.txt'

def main():

	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), FILE_NAME)) as input:
		fileInput = input.read().splitlines()[0]

		print(Part1.getStartPacketIdx(fileInput))
		print(Part2.getStartMessageIdx(fileInput))

		return 0

class Part1:

	def getStartPacketIdx(datastream: str):
		packetStartLen = 4
		buf: list = []

		for i in range(len(datastream)):
			buf.append(datastream[i])

			if (i >= packetStartLen - 1):

				# cast buf to a set to remove dupes
				x = set(buf)
				if (len(set(buf)) == packetStartLen):
					# we found a set of 4 with no dupes
					return i + 1

				# remove first element of buffer
				buf.pop(0)

		return 0

class Part2:

	def getStartMessageIdx(datastream: str):
		packetStartLen = 14
		buf: list = []

		for i in range(len(datastream)):
			buf.append(datastream[i])

			if (i >= packetStartLen - 1):

				# cast buf to a set to remove dupes
				x = set(buf)
				if (len(set(buf)) == packetStartLen):
					# we found a set of 4 with no dupes
					return i + 1

				# remove first element of buffer
				buf.pop(0)

		return 0


if __name__ == '__main__':
	main()