def print_list(seq):
    for x in seq : print(x, end=" ")
    print()


def main():
    seq = range(11)
    # 0 1 2 3 4 5 6 7 8 9 10
    print_list(seq)

    # 0 2 4 6 8 10 12 14 16 18 20
    print_list([x * 2 for x in seq])

    # 0 2 4 6 8 10
    print_list([x for x in seq if x % 2 == 0 ])


if __name__ == "__main__" : main()