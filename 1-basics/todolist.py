from asyncio import tasks
from tokenize import Number


print("Chose a todo list:")
print("Add task to list:")
print("Remove task from list:")
print("Exit:")


tasks =[]   
choice = int(input("Select what you want to do: "))


while True:
    if choice == 1:
        task = input("Add task: ")
        if task == -1:
            break
        tasks.append(task)
        print(tasks)

    elif choice == 2:
        task = input("Remove task: ")
        tasks.remove(task)
        print(tasks)
    elif choice == 3:
        exit()