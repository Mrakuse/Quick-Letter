import time as t
import random as r
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def pull():
    for i in range(5, -1, -1):
        print('СИМВОЛ ПОЯВИТСЯ ЧЕРЕЗ: ')
        print(i)
        t.sleep(1)
        cls()
    alphavit = 'qwertyuioplkjhgfdsazxcvbnm1234567890'
    sim = alphavit[r.randint(0, len(alphavit))]
    print('''-----------
-   ''', sim, '''   -
-----------
''')

    enter = ''
    count = 0
    s_time = t.monotonic()
    while enter.lower() != sim:
        count += 1
        enter = input()
        print()
    e_time = t.monotonic()
    seconds = e_time - s_time
    return count, seconds


print('''ДОБРО ПОЖАЛОВАТЬ В ИГРУ <<QUICK LETTER>>

СУТЬ ИГРЫ
На экран выводится случайный символ латинского алфавита(буква, цифра). 
Задача: как можно скорее ввести этот символ.

y - играть
иной символ - выйти''', '\n')
enter = input()

if enter.lower() != 'y':
    print('COME BACK')
    t.sleep(5)
    quit()

cls()
count, seconds = pull()