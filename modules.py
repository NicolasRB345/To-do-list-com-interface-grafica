import json
import os

def save(list, path):
    data = []
    with open(path, 'w', encoding='utf-8') as file:
        data = json.dump(
            list,
            file,
            ensure_ascii=False,
            indent=2
        )
    return data


def read(list, path):
    data = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        return  save(list, path)
    return data


def list(list_task):
    os.system('cls')
    try:
        if list_task == []:
            print("There are no tasks in your list.")

        for task in list_task:
            print(f'{list_task.index(task)} - {task}')

    except TypeError:
        print("There are no tasks in your list of tasks.")
        pass


def add(list, path):
    os.system('cls')
    try:
        task = input('Create a new task: ')
        list.append(task)
        save(list, path)
        print('New task added.')
    except AttributeError:
        print('Please, only for your first task add for the first time, I ask to you add it again :)')
        pass


def remove(list, list_trash, path, path_trash):
    os.system('cls')
    try:
        task = int(input("Remove task (Type its index): "))
    except ValueError:
        print('Please, type only numbers')
    
    try:
        task_removed = list.pop(task)
        list_trash.append(task_removed)
        save(list, path)
        save(list_trash, path_trash)
        print('Task was removed.')
    except IndexError:
        print("There's no task with this index")


def restore(list, list_trash, path, path_trash):
    os.system('cls')
    try:
        restored_task = list_trash[-1]
        list.append(restored_task)
        list_trash.pop()
        save(list, path)
        save(list_trash, path_trash)
        print(f'Task was restored as index: {len(list) - 1}')
    except IndexError:
        print("There are no tasks to restore.")


def see_Trash(list_trash):
    os.system('cls')
    if list_trash == []:
        print('There are no tasks to see in the Trash.')

    for task in list_trash:
        print(f'- {task}')


def clear_list(list, path):
    os.system('cls')
    if list == []:
        print('List of tasks is already cleared')

    else:
        while True:
            choice = input('Are you sure that you want to delete all tasks from your list of tasks? [Y/n]: ').upper()

            if choice == 'Y':
                list = []
                save(list, path)
                print('List of tasks was cleared.')
                break
            elif choice == 'N':
                print('Command cancelled.')
                break
            else:
                print('Please, type only Y or n')


def clear_trash(list_trash, path_trash):
    os.system('cls')
    if list_trash == []:
        print('The Trash is already cleared')

    else:
        while True:
            choice = input('Are you sure that you want to delete all tasks from the Trash? [Y/n]|: ').upper()

            if choice == 'Y':
                list_trash = []
                print('Trash was cleared.')
                save(list_trash, path_trash)
                break
            elif choice == 'N':
                print('Command was cancelled.')
                break
            else:
                print('Please, type only Y or N.')



   