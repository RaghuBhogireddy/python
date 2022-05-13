
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
    sentence = "Hello, evrydody, I'm Nick"
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


def format_string():
    print("{} has to get this job real {}".format("Raghu","quicker"))
    name = "Raghu"
    work = "quicker"

    print(f"{name} has to get this job real {work}")

def partition_string():
    s = "Hi there, how are you today"
    """Unlike string.split(), partition will divide sentence with 
    first occurence of the separator"""
    print(s.partition("are"))

def ljust_lstrip_string():
    s = "Raghu"
    s_1 = s.ljust(7,"*")
    print(s_1)
    print(len(s_1))
    print('------------------')
    s_2 = "      Raghu   "
    print(len(s_2))
    s_3 = s_2.lstrip()
    print(s_3)
    print(len(s_3))

def trailing_3(word):
    num = len(word)
    pad = (3 - num%3)*"*"
    print(word+pad)

def Rfind_Rsplit():
    s = "Hi There, how are you, I'm good"
    print(s.rfind("o"))
    print(s.rsplit("o",2))

def rjust_rindex():
    s = "aeiouatbi"
    print(s.rjust(12,"*"))
    print(s.rindex("i"))


def rstrip_rpartition():
    s = "     aeiouatbi     "
    print(s.rstrip())
    print(s.partition("a")) # partition based on first a
    print(s.rpartition("a")) # partition based on last a 


if __name__ == "__main__":
    # print(index_all("Raghu","Ra"))
    # split()
    # join()
    # make_list()
    # format_string()
    # partition_string()
    # ljust_lstrip_string()
    # trailing_3("raghu")
    # Rfind_Rsplit()
    # rjust_rindex()
    rstrip_rpartition()