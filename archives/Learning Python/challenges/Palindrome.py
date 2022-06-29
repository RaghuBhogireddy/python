run = True


def is_Palindrome(newstring):
    if newstring == newstring[::-1]:
        return True
    else:
        return False


while run:
    testString = input("Enter String to test for Palindrome or 'exit' : ")
    testString.lower()

    if testString == "exit":
        run = False
        break

    newString = ""
    for x in testString:
        if x.isalnum():
            newString += x

    print("palindrome Test : ", is_Palindrome(newString))
