
def main():
    """In this lab you will be concatenating a python string with string from a list.
    First you will be asked to sort the list. Then you are going to be asked to iterate through the
    sorted list and concatenate each item with the string greeting.
    Finally append concatenated string to the python list greetings."""

    names = ["Sam", "Paul", "John", "Matt"]
    greeting = "Hello, nice to meet you "
    names.sort()
    greetings = []
    for name in names:
        greet = greeting.strip() + ", " + name
        greetings.append(greet)

    print(greetings)


def index_all(letters,sub):
    index = []
    location = 0
    occerances = 0
    count = letters.count(sub)
    while occerances < count:
        index.append(letters.index(sub,location))
        occerances += 1
        location = letters.index(sub,location) + 1
    return index

def split():
    sentence = "Hello evrydody, I'm Nick"
    print(sentence.split(','))

def join():
    sentence = "Hello evrydody, I'm Nick"
    split = sentence.split(',') # ['Hello evrydody', " I'm Nick"]
    print(','.join(split))

def make_list():
    sentence = "Hello evrydody, I'm Nick"
    print(list(sentence))

list = []
def either(prefixes,words):
    for word in words:
        for pre in prefixes:
            if word.startswith(pre):
                list.append(word)
            else:
                continue


if __name__ == "__main__":
    # print(index_all("Raghu","Ra"))
    # split()
    # join()

    make_list()