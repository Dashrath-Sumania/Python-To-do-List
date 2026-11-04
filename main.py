import utils

print("---Your To-do List---")
print("Press help for list of commands")

path = "database.txt"

tasks = utils.load_tasks(path)

while True:
    query = input("> ")
    query = query.split(maxsplit=1)
    command = query[0].lower()
    has_task = False
    if len(query) > 1:
        task = query[1]
        has_task = True

    if command == "quit":
        break
    elif command == "help":
        print("1. List \n2. Create {task} \n3. Remove {task} \n4. Quit")
    elif command == "list":
        n = 1
        for i in tasks:
            print(f"{n}. {i}")
            n += 1
    elif command == "create":
        if has_task:
            tasks.append(task)
            utils.add_task(task, path)
            print("Task created successfully")
        else:
            print("Error: Command requires an argument")
    elif command == "remove":
        if has_task:
            tasks = [i for i in tasks if i != task]
            utils.remove_task(task, path)
            print("Task removed successfully")
        else:
            print("Error: Command requires an argument")  
    else:
        print("Invalid Command")

print("Thankyou for using this program")
