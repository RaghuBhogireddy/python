def main(S):
    return ''.join([i  for i in S if i!= ' '])

if __name__ == "__main__":
    print(main("    hello there   "))