import random
import time

def guess_game():
    print("Hi!. Welcome to guessing game. I'll a pick a number now between 1 and 100.")
    time.sleep(3)
    print("Picking a number ...")
    time.sleep(2)
    pick = random.randint(1,100)
    guess = int(input("what is you guess ? "))
    guess_count = 1
    
    while(guess != pick):
        guess_count += 1
        if guess < pick:
            guess = int(input("Wrong. you need to guess high. What is your guess ? "))
        else:
            guess = int(input("Wrong. you need to guess low. What is your guess ? "))

    print(f"Correct. It took {guess_count} times to guess the {pick}")

guess_game()