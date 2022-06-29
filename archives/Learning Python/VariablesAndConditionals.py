def main():
    print("Welcome To play Ground")


# Invocation
if __name__ == "__main__":
    main()

myInt = 5
myFloat = 13.2
myString = "Hello"
myBool = True
myList = [0, 1, "Two", 3.4, 78, 89, 45, 67]
myTuple = (0, 1, 2)
myDict = {"one": 1, "Two": 2}

# Random print Statements
print(myDict)
print(myTuple)
print(myInt)
print(myList)
print(myFloat)
print(myString)

# Slicing in list
print(myList)
print(myList[2:5])
print(myList[::-1])
print(myList[:5])
print(myList[5])

# Dicts Accessing via keys
print(myDict["Two"])

# Error : Variables of Different Types can't be Combined
print("String" + str(123))


# Global vs Local Variables
def some():
    myString = "inside function"
    print(myString)


def addition(arg1, arg2):  # for default args we can use like =>  function(arg1, arg2=x) :
    result = 1
    for i in range(arg2):
        result = result * arg1
    return result


def multiArg(*args):  # we can have multiple args with multi, but it should always atLast
    result = 0
    for x in args:
        result = result + x
    return result


def conditionals():
    x, y = 10, 100
    result = "x is greater" if x > y else "y is greater"
    value = "three"
    match value:
        case "one":
            result = 1
        case "two":
            result = 2
        case "three" | "four":
            result = (3, 4)
        case _:
            result = -1
    print(result)
    print("---------")
    x = 0
    while x < 5:
        print(x)
        x = x + 1
    print("---------")
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days:
        print(day)
    print("---------")
    for x in range(5, 10):
        # if x == 7:
        #     break
        if x % 2 == 0:
            continue
    print(x)
    print("---------")
    for i, d in enumerate(days):
        print(i, d)
    print("---------")


some()
print("============")
print(myString)
print("============")
print(some())
print("============")
print(addition(2, 10))
print("============")
print(multiArg(2, 3, 4, 5, 6, 4))
print("============")
conditionals()
print("============")
