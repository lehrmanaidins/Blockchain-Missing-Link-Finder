
'''
    JSON Blockchain Missing Link
'''

import json

def main():
    with open(u'testchain.txt', 'rt', encoding='utf-8') as file:
        block_chain = json.loads(file.read())

        for i in range(1, block_chain['length']):
            if (i != block_chain['chain'][i - 1]['index']):
                print(i)
                break

if __name__ == '__main__':
    main()
    