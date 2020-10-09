"""Prompt user for a target date."""

from functions import (todays_date,
                       prompt_user_for_target_date)

while True:
    target_date = prompt_user_for_target_date("\nEnter a target date in "
                                              "YYYY-MM-DD format\n> ")
    if target_date > todays_date:
        FILE = open("target_date.txt", "w")
        FILE.write(str(target_date))
    else:
        print("Please enter a date in the future.")
