import sys
import requests
import os

"""
Carson Rohan
AOC2022
Module for creating necessary day files and getting input because I'm lazy.
"""

STATUS_OK = 200
AOC_INPUT_URL = 'https://adventofcode.com/2022/day/?/input'
URL = 'https://adventofcode.com/2022'
COOKIES = {
    'ru': '53616c7465645f5f2c67d612a845a9fcdc07298538ebd2682ed70370db6628b9339c2b44f0ac9f6ddda8c328c019e2a7',
    'session': '53616c7465645f5f23018bfd020806f650900995c24f0b6c2c15daeb7a7a0a96b8e7cead4e49d6e459eb9484221147c65c40d03de7200eb481312e500ea999eb'
}

INPUT_SIZE = 2
DAY_TEMPLATE = '"""\nCarson Rohan\nAOC2022\nDay Part: Name_of_puzzle\n"""\n\nimport os\n\nFILE_NAME = \'d?i.txt\'\n\ndef main():\n\treturn 0\n\nclass Part1:\n\n\tdef blah():\n\t\treturn 0\n\nif __name__ == \'__main__\':\n\tmain()'

def main():

    # error checking
    if (len(sys.argv) != INPUT_SIZE):
        print('Usage: %s <day #>'%(os.path.basename(__file__)))
        return

    if (not sys.argv[INPUT_SIZE - 1].isdigit()):
        print('Input must be integer')
        return

    # prep for 
    day = sys.argv[INPUT_SIZE - 1]

    cookiesForHeader = ''.join(f'{key}={value};' for key, value in COOKIES.items())[:-1]

    header = {
        'Accept': '*/*',
        'Host': 'Me',
        'User-Agent': 'Python/3.6.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Cookie': cookiesForHeader
    }

    response = requests.get(AOC_INPUT_URL.replace('?', day), headers=header)

    if (response.status_code != STATUS_OK):
        print(response.status_code)
        return

    # create dirs/files
    parentDir = os.path.dirname(os.path.abspath(__file__))
    dayDir = os.path.join(parentDir, r'../d%s'%(day))
    inputFile = os.path.join(dayDir, r'd%si.txt'%(day))
    dayFile = os.path.join(dayDir, r'd%s.py'%(day))

    if (not os.path.exists(dayDir)):
        os.mkdir(dayDir)

    if (not os.path.exists(inputFile)):
        with open(inputFile, 'w') as input:
            input.write(response.text)

    if (not os.path.exists(dayFile)):
        with open(dayFile, 'w') as p1:
            p1.write(DAY_TEMPLATE)

    return 0

if __name__ == '__main__':
    main()
