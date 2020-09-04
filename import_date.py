"""Import target date."""

import datetime


def get_target_date():
    """Import target_date from "target_date.txt".""""

    date_file = open("target_date.txt", "r")
    imported_target_date = date_file.read()
    datetime_obj = datetime.datetime.strptime(imported_target_date, "%Y-%m-%d")
    return datetime_obj.date()


target_date = get_target_date()
