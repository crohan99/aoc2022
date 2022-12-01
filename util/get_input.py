import sys
import requests
import os


STATUS_OK = 200
INPUT_SIZE = 2
AOC_INPUT_URL = 'https://adventofcode.com/2022/day/1/input'
URL = 'https://adventofcode.com/2022'
COOKIES = {
    'ru': '53616c7465645f5f2c67d612a845a9fcdc07298538ebd2682ed70370db6628b9339c2b44f0ac9f6ddda8c328c019e2a7',
    'session': '53616c7465645f5f69d41fe9274fd72a959d820cfa3e493c8ef3c18bd66f1ae6ad3df03cfd93e092ad1fe67c8373dfb3db8581600c17d1b500253548f5e48418'
}

def main():

    if (len(sys.argv) != INPUT_SIZE):
        print('Usage: get_input.py <day #>')
        return

    if (not sys.argv[INPUT_SIZE - 1].isdigit()):
        print('Input must be integer')
        return

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

    response = requests.get(AOC_INPUT_URL, headers=header)

    if (response.status_code != STATUS_OK):
        print(response.status_code)
        return

    if (not os.path.exists(os.path.dirname(os.path.abspath(__file__)) + r'/../d%s')):
        os.mkdir(os.path.dirname(os.path.abspath(__file__)) + r'/../d%s')

    with open(os.path.dirname(os.path.abspath(__file__)) + r'/../d%s/test_d%si%s.txt'%(day, day, day), 'w') as input:
        input.write(response.text)

    return 0

if __name__ == '__main__':
    main()