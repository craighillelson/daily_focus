"""Script to track daily tasks in pursuit of a goal."""

from functions import (target_date,
                       days_out,
                       todays_date,
                       dates_tasks,
                       diff_dates,
                       greeting,
                       tasks,
                       write_dct_to_csv)

greeting()
print("\ntarget date:", target_date)
print(f"90 days out: {days_out(90)}")
print(f"180 days out: {days_out(180)}")
to_do_today = tasks("What would you like to work on today?\n> ")
dates_tasks[todays_date] = to_do_today
write_dct_to_csv("dates_tasks.csv", dates_tasks)
days_from_target = diff_dates()
print(f"days from target: {days_from_target}\n")
