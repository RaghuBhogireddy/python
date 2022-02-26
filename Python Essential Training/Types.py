
from decimal import *

# We can use .format() function for String
# Else we can use fString with some variables assign as below
def main():
    x = 'seven {} {}'.format(8,9) # using .format() on String
    print("x is {}".format(x))

    a = 3
    b = 5
    x = f'seven {a} {b}'
    print("x is {}".format(x))

    # We can use some shift alignments as well for the values with both print formats
    x = f'seven {a:>06} {b:<06}'
    print("x is {}".format(x))
    print(type(x))

    x = .1 + .1 + .1 # This gives 0.300000000004 which is not accurate but precise. This can't be used in Money

    #solution: We can use 'decimal' Module which can have accuracy for transaction purposes
    a = Decimal('0.10')
    b = Decimal('0.30')
    x = a + a + a - b
    print(x)


    ## All Sequence Types can have multiple data TYpes
    # Sequence Types : Lists
    x = [1, 2, 'three', 4, 5]
    for i in x:
        print('x is {}'.format(i))

    print('============')
    # Sequence Types : Tuples -> immutable
    x = {1, 2, 3, 4, 'five'}
    for i in x:
        print('x is {}'.format(i))

    print('============')
    # Sequence Types : Range -> immutable. if we want to change data create list(range(n))
    for i in range(3):
        print('x is {}'.format(i))

    print('============')
    # Sequence Types : Dictonaries -> sequence of key value pairs
    x = {'one' : 1, 'two' : 2, 'three' : 'three'}
    for k,v in x.items():
        print('k: {}, v:{}'.format(k, v))

    print('============')
    # Type & Id
    # type(), id()
    x = (1, 'two', 3.0,[4, 'four'], 5)
    for j in x :
        print(type(j))


    print('============')
    # To check objects equality, we can use isinstance()
    if isinstance(x, tuple):
        print('yep')

x = 7 > 5
print(x)


if __name__ == "__main__" : main()