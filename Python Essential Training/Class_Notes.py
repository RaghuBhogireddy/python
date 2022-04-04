class Duck:
    sound = "quack quack !"
    color = " white mostly"

    def say(self):
        print(self.sound)



def main():
    donald = Duck()
    donald.say()


if __name__ == "__main__" : main()
