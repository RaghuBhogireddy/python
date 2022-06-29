
def main():
    secret = "password"
    pw = ""
    auth = False
    count = 0
    max_count = 5

    while pw != secret:
        count += 1
        if count >= max_count : break
        pw = input(f'{count}: Enter your secret : ')
    else:
        auth = True

    print("Authorized" if auth else "Calling FBI....")




if __name__ == "__main__": main()