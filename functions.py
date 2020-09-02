"""Functions"""

import csv
from datetime import (date,
                      timedelta)

target_date = date(2021, 8, 7)
todays_date = date.today()
dates_tasks = {}


def days_out(num_days):
    """Find the date a given number of days from the target date."""
    return (target_date - timedelta(days=num_days)).isoformat()


def diff_dates():
    """Return the number of days between the target date and today."""
    return abs((target_date - todays_date).days)


def greeting():
    """Greet user."""
    print("\nGood morning!")


def tasks(user_prompt):
    """Prompt user for input."""
    return input(f"\n{user_prompt}")


def write_dct_to_csv(file, dct):
    """Write dictionary to csv."""

    with open(file, 'w') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(["date", "task_start_of_day"])
        for today, task in dct.items():
            keys_values = (today, task)
            out_csv.writerow(keys_values)

    print(f'\n"{file}" exported successfully\n')
