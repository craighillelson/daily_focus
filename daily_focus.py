"""Script to track daily tasks in pursuit of a goal."""

from functions import (target_date,
                       todays_date,
                       date_tasks_to_add,
                       dates_tasks,
                       open_csv_pop_dct,
                       days_out,
                       diff_dates,
                       greeting,
                       prompt_user_for_task,
                       write_dct_to_csv)

dates_tasks_from_file = open_csv_pop_dct()
greeting()
print("\ntarget date:", target_date)
print(f"90 days out: {days_out(90)}")
print(f"180 days out: {days_out(180)}")
print(f"270 days out: {days_out(270)}")
to_do_today = prompt_user_for_task("What would you like to work on today?\n> ")
if dates_tasks_from_file:
    date_tasks_to_add[todays_date] = to_do_today
    dates_tasks = {**dates_tasks_from_file, **date_tasks_to_add}
else:
    dates_tasks[todays_date] = to_do_today
write_dct_to_csv("dates_tasks.csv", dates_tasks)
days_from_target = diff_dates()
print(f"days from target: {days_from_target}\n")
