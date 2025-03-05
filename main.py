from modules import *
import os

PATH_NAME_LIST = 'data_list.json'
PATH_NAME_LIST_TRASH = 'data_list_trash.json'

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
        command = int(input('Choose one of the commands above: '))
    except ValueError:
        os.system('cls')
        print('Please, type only numbers.')
        continue

    if command == 0:
        list(list_tasks)

    elif command == 1:
        add(list_tasks, PATH_NAME_LIST)

    elif command == 2:
        remove(list_tasks, list_trash, PATH_NAME_LIST, PATH_NAME_LIST_TRASH)

    elif command == 3:
        restore(list_tasks, list_trash, PATH_NAME_LIST, PATH_NAME_LIST_TRASH)

    elif command == 4:
        see_Trash(list_trash)

    elif command == 5:
        clear_list(list_tasks, PATH_NAME_LIST)

    elif command == 6:
        clear_trash(list_trash, PATH_NAME_LIST_TRASH)
    
    elif command == 7:
        print('See you soon :)')
        break
    
    else:
        os.system('cls')
        print('Please, type only a valid command.')
        continue