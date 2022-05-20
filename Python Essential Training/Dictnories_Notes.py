def printDict(dict):
    print('======= Type 1 =======')
    for d in dict :
        print('{} : {}'.format(d, dict[d]))
    print('======= Type 2 =======')
    for k , v in dict.items():
        print(f'{k} : {v}')


def main():
    dictionary = {"Kitten" : "meow", "dog" : "bark", "lion" : "roar"}
    # we can assign a dictionary is below method as well
    animals = dict(Kitten = "meow", dog = "bark", lion = "roar")
    printDict(dictionary)



if __name__ == "__main__": main()