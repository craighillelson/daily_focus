"""List dates and tasks."""

from functions import (open_csv_pop_dct,
                       output_dct)

dates_tasks_from_file = open_csv_pop_dct()
output_dct(dates_tasks_from_file)
