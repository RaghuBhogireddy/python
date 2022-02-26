import platform

# Different print() formats
print("This is python {}".format(platform.python_version()))
print(f"Hello World, {platform.python_version()}")

num = 43
def isprime(n):
    if n<=1:
        return False
    for x in (2,n):
        if n % x == 0:
            return False
        else:
            return True

if isprime(num) :
    print(f"{num}, is prime")
else:
    print(f"{num}, is not prime")


class Duck:
    def quack(self):
        print("Quacck!")

    def walk(self):
        print("Walks like a duck")

def main():
    donald = Duck()
    donald.walk()
    donald.quack()


if __name__ == "__main__" : main()



