def printSet(set):
    sorted(set)
    print('{', end=" ")
    for x in set :
        print(x, end=" ")
    print('}')


def main():
    a = set("Hi There, Raghuram")
    b = set("Hello, Nice to Meet you")
    x = set('hello')
    y = set('world')
    printSet(a)
    printSet(b)
    printSet(x - y )

if __name__ == "__main__": main()