def solution():
    for n in range(1,100):
        if n % 15 == 0:
            print('FizzBuzz')
        elif n % 3 == 0:
            print('Fizz')
        elif n % 5 == 0:
            print('Buzz')
        else:
            print(n)

#solution()

from datetime import datetime

def def_pass():
    print(f'current-pass: {datetime.now().second}')
    wait_until = datetime.now().second + 4

    while datetime.now().second != wait_until:
        pass

    print(f"Waited until {wait_until} seconds")

def_pass()

def def_break():
    print(f'current-break: {datetime.now().second}')
    wait_until = datetime.now().second + 4

    while True:
        if datetime.now().second == wait_until:
            break


    print(f"Waited until {wait_until} seconds")

def_break()

def def_continue():
    print(f'current-continue: {datetime.now().second}')
    wait_until = datetime.now().second + 4

    while datetime.now().second != wait_until:
        continue

    print(f"Waited until {wait_until} seconds")

def_continue()