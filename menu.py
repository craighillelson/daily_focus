"""Present user with a list of options."""

import pyinputplus as pyip

options_map = {
    "enter daily focus": "daily_focus.py",
    "list dates and tasks": "list.py",
    "quit": "quit",
}

options = list(options_map.keys())

while True:
    print("\nPlease choose an option below.")
    for num, option in enumerate(options, 1):
        print(num, option)
    user_choice = pyip.inputMenu(options, numbered=True, prompt="> ")
    if user_choice != "quit":
        exec(open(options_map[user_choice]).read())
    else:
        break
