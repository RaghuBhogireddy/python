
import random

print(random.randint(1,18))

# make own version of magic 8 that print yes, no or maybe
# each time when you ask it

ans = random.randint(1,3)
if ans == 1: print("Yes")
if ans == 2: print("No")
if ans == 3: print("May be")


"""
    Fortune Cookie : Project 1
"""
# Fortune Cookie
lucky_number = random.randint(1,100)
fortune_number = random.randint(1,3)
fortune_text = ''

if fortune_number == 1 : fortune_text = "You will have good day"
if fortune_number == 2 : fortune_text = "Things will be tough for you"
if fortune_number == 3 : fortune_text = "You get a easy going today"

print(f'{fortune_text}, your lucky number is : {lucky_number}')

"""

    Lists, Loops, Dictonaries    
    
"""

""" List """
sequence = ['a', "b", 3, 4.5]
# list insert
sequence.insert(2,1000)
sequence.append(999)
print(sequence)

# access items in list
print(sequence[1])

# find length
print(len(sequence))

""" Loops """
for seq in sequence:
    print(seq)

""" Dictonary """



