import urllib.request, json
import sys

INPUT_SIZE = 2
AOC_INPUT_URL = 'https://adventofcode.com/2022/day/?/input'

def main():

    print(len(sys.argv))

    if (len(sys.argv) != INPUT_SIZE and not sys.argv[INPUT_SIZE - 1].isdigit()):
        print('Usage: get_input.py <day #>')
        return

    day = sys.argv[INPUT_SIZE - 1]

    with urllib.request.urlopen(AOC_INPUT_URL.replace('?', day)) as url:
        data = json.load(url)
        print(data) 

    return 0

if __name__ == "__main__":
    main()