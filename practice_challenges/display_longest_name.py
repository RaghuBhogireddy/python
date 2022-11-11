def main(str):
    longest = ""
    for name in str:
        if len(longest) <= len(name):
            longest = name
    return longest


if __name__ == "__main__":
    print(main(["Geek", "For", "Geeks", "GeeksForGeeks"])) 