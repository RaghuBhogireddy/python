


def main():
    lists()
    tuples()
    dictionaries()

def lists():
    # Lists are mutable means we can alter the data in the List Object
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spark']
    # We can add items using append
    game.append('Cricket')
    print(game)
    print('=====================')
    # To insert at particuar position
    game.insert(2,'Hockey')
    print(game)
    print('=====================')
    # To remove specific Item using remove() or using it's index in pop() or we can use del statement
    game.remove('Paper')
    print(game)
    print('=====================')
    game.pop(3)
    print(game)
    print('=====================')
    del game[3]
    print(game)
    print('=====================')

def tuples():
    # Tuples are immutable, so we can't perform any modificationson the tuple.
    # Only we can get info about the Object
    game = ('Rock', 'Paper', 'Scissors', 'Lizard', 'Spark')


def dictionaries():
    animals = {'Kitty' : 'meow', 'puppy' : 'ruff!', 'lion' : 'grr', 'dragon' : 'rawr'}
    print(animals)


if __name__ == "__main__" : main()