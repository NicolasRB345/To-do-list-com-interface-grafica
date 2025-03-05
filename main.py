from modules import *
import os

PATH_NAME_LIST = 'data_list.json'
PATH_NAME_LIST_TRASH = 'data_list_trash.json'
LIST_OF_COMMANDS = [0, 1, 2, 3, 4, 5, 6, 7]

while True:
    list_tasks = read([], PATH_NAME_LIST)
    list_trash = read([], PATH_NAME_LIST_TRASH )

    print()
    print('[0] List tasks 📜')
    print('[1] Add task 📌')
    print('[2] Remove task 🚮')
    print('[3] Restore last task removed 📃')
    print('[4] See Trash  🗑️')
    print('[5] Clear list 🧹📜')
    print('[6] Clear Trash 🧹🗑️')
    print('[7] Quit the program 👋')

    try:
        command = int(input("Choose one of the number's command above: "))
    except ValueError:
        os.system('cls')
        print('Invalid command!')
        continue

    commands = {
        0 : lambda: list(list_tasks),
        1 : lambda: add(list_tasks, PATH_NAME_LIST),
        2 : lambda: remove(list_tasks, list_trash, PATH_NAME_LIST, PATH_NAME_LIST_TRASH),
        3 : lambda: restore(list_tasks, list_trash, PATH_NAME_LIST, PATH_NAME_LIST_TRASH),
        4 : lambda: see_Trash(list_trash),
        5 : lambda: clear_list(list_tasks, PATH_NAME_LIST),
        6 : lambda: clear_trash(list_trash, PATH_NAME_LIST_TRASH)
    }

    if command == 7:
        os.system('cls')
        print('See you soon :)')
        break

    if command not in LIST_OF_COMMANDS:
        os.system('cls')
        print('Invalid command!')
        continue


    command_choice = commands.get(command)()

    
