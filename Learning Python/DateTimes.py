from datetime import time
from datetime import date
from datetime import datetime
from datetime import timedelta
import calendar


def dateTime():
    today = date.today()
    print("Today's date is", today)
    print("Date Components : #", today.day, today.month, today.year)
    print("Today's WeekDay :", today.weekday())

    print("===================")

    today_1 = datetime.now()
    print("Time is :", today_1)
    print("Current Time is :", datetime.time(today_1))

    print("=======Date Formatting============")

    # %y/%Y - Year,
    # %a/%A - weekday,
    # %b/%B - month,
    # %d - day of Month

    print(today_1.strftime("%A, %d %B, %yY"))

    print("=======Date Formatting============")
    # %c - local date & time,
    # %x - locale's date,
    # %X - Locale's time

    print(today_1.strftime("%c"))

    print("=======Time Formatting============")

    # %I/%H - 12/24, %M - Minute, %S - Second, %p - locale's AM/PM
    print(datetime.now().strftime("%H:%M:%S.%p"))


def timeDelta():
    print(timedelta(days=365, hours=5, minutes=1))

    now = datetime.now()
    print("Today is ", now)
    print("One year from now will be,", str(now+timedelta(days=365)))
    print("In Two Weeks & Three Days, Time will be,", str(now+timedelta(weeks=2, days=3)))
    print("Two Weeks back the date is,", str((now-timedelta(weeks=2)).strftime("%x")))
    today = date.today()
    afd = date(today.year, 4, 1)
    if afd < today:
        print("April's Fools Day already went by")
    else:
        print("Time to April Fool's Day is ", afd - today)


def calendars():
    c = calendar.TextCalendar(calendar.SUNDAY)
    formatted = c.formatmonth(2021, 1, 0, 0)
    print(formatted)


if __name__ == "__main__":
    calendars()
