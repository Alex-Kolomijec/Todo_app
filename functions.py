# Function for open the txt file and return the list of todos
def get_todos(filepath="todos.txt"):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


# Function for the writing new todos into the txt file
def write_todos(todos_arg, filepath="todos.txt"):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)