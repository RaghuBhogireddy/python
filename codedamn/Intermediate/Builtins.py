


def main():
    print(sum(list(range(5))))
    print(pow(2,3))

def exp(root,power):
    """ root^power returns string of equation"""
    base = " x ".join(str(root)*power)
    print(  chr(ord('c')))
    return f"{base} = {pow(root,power)}"

def enumerate_():
    l = ["aff","adasf","asdasc"]
    print(list(enumerate(l,2)))

def zip_():
    l = list(range(3))
    x = "abx"
    print(list(zip(x,l)))


if __name__ == "__main__":
   print(exp(4,5))
   enumerate_()
   zip_()