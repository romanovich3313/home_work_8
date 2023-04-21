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
    {'name': 'Oleg', 'birthday': datetime(1900, 4, 9)},
    {'name': 'Slava', 'birthday': datetime(1995, 8, 11)},
    {'name': 'Roma', 'birthday': datetime(1995, 8, 11)},
    {'name': 'Bob', 'birthday': datetime(2000, 1, 16)},
    {'name': 'Nata', 'birthday': datetime(2002, 6, 20)},
    {'name': 'Maria', 'birthday': datetime(2002, 6, 9)},
    {'name': 'Petro', 'birthday': datetime(2000, 1, 8)},
    {'name': 'Nastia', 'birthday': datetime(1998, 4, 2)}
]))
