from time_module import get_hours, get_date
from output_module import output
from database import update_last_seen, get_last_seen


def greet():
    previous_date = get_last_seen()

    today_date = get_date()
    update_last_seen(today_date)

    if previous_date == today_date:
        output("Welcome back Sir")
    else:
        hour = int(get_hours())
        if 4 <= hour < 12:
            output("Good Morning Sir ")

        elif 12 <= hour < 16:
            output("GOOD After Noon Sir")

        else:
            output("Good evening")
