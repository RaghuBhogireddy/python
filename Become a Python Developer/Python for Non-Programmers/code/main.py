
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
print("###########")
cats = {"Jane": 7, "Rag":5, "kitty": 8}
for cat, age in cats.items():
    print(cat+":"+ str(age))

print("###################")
print("Word Count")

text = """
    In this course, Nick teaches the fundamentals of Python to you: a non-programmer, 
    a user with little to no coding experience. Learn more about what Python is, and what it is and 
    isn’t used for. Explore how Python works with numbers and how you can interact with simple programs such 
    as a simple number-guessing game. Find out how to work with text in Python by building a reusable function 
    to count the words in a block of text. And along the way, 
    tackle quick challenges and other games that allow you to put your new skills to the test.
"""

word_count = {}

for word in text.lower().split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)


print("######")
print("---- Functions -------")

def dog(name):
    return f"{name} : Woof Woof"

print(dog("ted"))

number = input("number: ")
print(number + 2)


