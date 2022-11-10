def main(str):
    for i in str:
        if int(i) != 0 and int(i) != 1:
            return 0
        
    return 1


if __name__ == "__main__":
    print(main("34315"))