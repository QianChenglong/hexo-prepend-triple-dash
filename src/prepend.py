# coding: utf-8


import os
import sys
from colorama import init, Fore

init(autoreset=True)

skip_count = 0
prepend_count = 0

def prepend(filename):
    global skip_count, prepend_count
    fp = open(filename, 'rb')
    lines = fp.readlines()
    if lines[0].startswith('---'):
        skip_count += 1
        print('{:75s}'.format(filename) + Fore.RED + 'skip')
        return
    else:
        prepend_count += 1
        print('{:72s}'.format(filename) + Fore.GREEN + 'prepend')
        lines[0] = '---\n' + lines[0]
    fp.close()

    fp = open(filename, 'wb')
    fp.writelines(lines)
    fp.close()

def print_count():
    print('-' * 79)
    sys.stdout.write(Fore.RED + '{:10s}'.format('skip: '))
    print(skip_count)
    sys.stdout.write(Fore.GREEN + '{:10s}'.format('prepend: '))
    print(prepend_count)

def main():
    for root, dirs, files in os.walk('.'):
        for filename in files:
            if filename.endswith('.md'):
                prepend(filename)

    print_count()

if __name__ == '__main__':
    main()
