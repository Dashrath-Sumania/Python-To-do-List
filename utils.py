def load_tasks(path: str)->list[str]:
    task_list = []
    with open(path, "r") as file:
        for line in file:
            line = line.strip("\n")
            task_list.append(line)
    return task_list

def add_task(task: str, path: str)->None:
    with open(path, "a") as file:
        file.write(task + "\n")

def remove_task(task: str, path: str)->None:
    tasks = load_tasks(path)

    with open(path, "w") as file:
        for element in tasks:
            if element != task:
                file.write(element + "\n")
