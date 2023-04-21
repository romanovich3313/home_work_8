from datetime import datetime, timedelta


def get_birthdays_per_week(users):

    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]

    birthdays_per_weekday = {weekday: [] for weekday in weekdays}

    today = datetime.now()

    for user in users:
        name = user["name"]
        birthday = user["birthday"]

        for i in range(0, 7):
            next_weekday = today + timedelta(days=i)
            if next_weekday.strftime("%A") == birthday.strftime("%A"):
                birthdays_per_weekday[next_weekday.strftime("%A")].append(name)

    for weekday in weekdays:
        names = ", ".join(birthdays_per_weekday[weekday])
        if names:
            print(f"{weekday}: {names}")


print(get_birthdays_per_week([
    {'name': 'Oleg', 'birthday': datetime(year=1900, month=4, day=9)},
    {'name': 'Slava', 'birthday': datetime(year=1995, month=8, day=11)},
    {'name': 'Roma', 'birthday': datetime(year=1995, month=8, day=11)},
    {'name': 'Bob', 'birthday': datetime(year=2000, month=1, day=16)},
    {'name': 'Nata', 'birthday': datetime(year=2002, month=6, day=20)},
    {'name': 'Maria', 'birthday': datetime(year=2002, month=6, day=9)},
    {'name': 'Petro', 'birthday': datetime(year=2000, month=1, day=8)},
    {'name': 'Nastia', 'birthday': datetime(year=1998, month=4, day=2)}
]))
