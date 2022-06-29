import math


def square(num):
    print(math.sqrt(num))


square(16)

# Handling Exceptions
try:
    answer = input("What should I divid 10 by ?")
    num = int(answer)
    print(10/num)
except ZeroDivisionError as e:
    print("You can't divide by 0")
except ValueError as e:
    print("please provide a valid number")
    print(e)
finally:
    print("Code ran successfully")

# if __name__ == "__main__":
#     square(16)
