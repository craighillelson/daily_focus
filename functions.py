"""Functions."""

import csv
import datetime
from datetime import (date,
                      timedelta)
import pyinputplus as pyip

target_date = date(2021, 8, 7)
todays_date = date.today()
date_tasks_to_add = {}
dates_tasks = {}


def days_out(num_days):
    """Find the date a given number of days from the target date."""
    return (target_date - timedelta(days=num_days)).isoformat()


def diff_dates():
    """Return the number of days between the target date and today."""
    return abs((target_date - todays_date).days)


def get_target_date():
    """Import "target_date.txt" and return the date contained in the file."""

    date_file = open("target_date.txt", "r")
    imported_target_date = date_file.read()
    datetime_obj = datetime.datetime.strptime(imported_target_date, "%Y-%m-%d")
    return datetime_obj.date()


def greeting():
    """Greet user."""
    print("\nGood morning!")


def open_csv_pop_dct():
    """Open csv and populate a dictionary with its contents."""

    dct = {}

    with open("dates_tasks.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dct[row["date"]] = row["task_start_of_day"]

    return dct


def prompt_user_for_target_date(user_prompt):
    """Prompt user for target date."""
    return pyip.inputDate(user_prompt, formats=["%Y-%m-%d"])


def prompt_user_for_task(user_prompt):
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
