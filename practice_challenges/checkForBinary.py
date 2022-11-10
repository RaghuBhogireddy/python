def main(str):
    flag = 0
    #binary = [i for i in str]
    for i in str:
        if int(i) == 0 or int(i) == 1:
            pass
        else :
            flag = 1
        
    if flag == 1 : return 0
    else: return 1


if __name__ == "__main__":
    print(main("10000100010"))