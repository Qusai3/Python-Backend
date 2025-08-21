from datetime import datetime, timedelta

def time_until_birthday(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    today = datetime.today().date()

    next_birthday = birthdate.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)

    delta = datetime.combine(next_birthday, datetime.min.time()) - datetime.now()

    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return days, hours, minutes

birthdate_input = "2000-08-25"
d, h, m = time_until_birthday(birthdate_input)
print(f"Time until next birthday: {d} days, {h} hours, {m} minutes")