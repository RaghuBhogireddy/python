import calendar


run = True


def countdays(year, month, day):
    dayCount = 0
    weekList = calendar.monthcalendar(year, month)
    for week in weekList:
        if week(day) != 0:
            dayCount += 1
    return dayCount


while(run):
    try:
        print("Which day of the week do you want to count?")
        print("0: Monday")
        print("1: Tuesday")
        print("2: Wednesday")
        print("3: Thursday")
        print("4: Friday")
        print("5: Saturday")
        print("6: Sunday")
        print(" OR 'exit' to quit")

        theday = input("? ")
        if theday == "exit":
            run = False
            break
        day = int(theday)
        year = int(input("Enter year: "))
        month = int(input("Enter month: "))

        result = countdays(year, month, day)
        print("There are" + str(result) + " of those days in the month % year specified")
        print("--------------\n")
    except Exception as e:
        print("Not a valid one")
        print(e)