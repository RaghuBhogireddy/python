

def main():
    hungry = True
    # This Explains the ternary concept in Python
    x = 'Feed the bear now' if hungry else 'Don\'t feed the bear'
    print(x)


    # Bitwise Operators
    a = 0x0a
    b = 0x01

    c = a << b
    print(f'(hex) a is {a:02x}, b is {b:02x}, c is {c:02x}')
    print(f'(bin) a is {a:08b}, b is {b:08b}, c is {c:08b}')

    c = a & b
    print(f'(hex) a is {a:02x}, b is {b:02x}, c is {c:02x}')
    print(f'(bin) a is {a:08b}, b is {b:08b}, c is {c:08b}')

    c = a | b
    print(f'(hex) a is {a:02x}, b is {b:02x}, c is {c:02x}')
    print(f'(bin) a is {a:08b}, b is {b:08b}, c is {c:08b}')

    c = a ^ b
    print(f'(hex) a is {a:02x}, b is {b:02x}, c is {c:02x}')
    print(f'(bin) a is {a:08b}, b is {b:08b}, c is {c:08b}')

    # Boolean Operators
    # and     -> And
    # or      -> Or
    # not     -> Not
    # in      -> Value in set
    # not in  -> Value not in set
    # is      -> Same Object identity
    # is not  -> Not same object identity

    a = ('bear', 'bunny', 'tree', 'sky', 'rain')
    b = 'bear'

    # We can have else block with while or for loops

if __name__ == "__main__" : main()