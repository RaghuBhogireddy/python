

def Func(a, b):
    a=1 ; b[0]=1
x=0 ; y=[0]
Func(x, y)
print(x, y)

def main():
    x = ('meow', 'chi', 'shark')
    kitten()
    #kitten2(Buffy = 'meow', zilla = 'grr')

def kitten(*args):
    if len(args):
        for i in args:
            print(f'Kitten {i} ')

def kitten2(**kwargs):
    if len(kwargs):
        for i in kwargs:
            print(f'Kitten {i} ')

if __name__ == "__main__" : main()