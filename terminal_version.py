# Importing functions from the script
from functions import get_todos, write_todos

# Start the while loop
while True:
    # Take user's input for the following commands
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    # First is "add" function, which adds new todos to the list
    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)

    # Second is show function which shows the list of todos
    elif user_action.startswith("show"):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n").title()
            # Add 1 to index because in python position starts with 0
            row = f"{index + 1}-{item}"
            print(row)

    # This part allows to edit any of todos
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            # reformatting to python numeration
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            write_todos(todos)
        # In case user input something different from the number
        except ValueError:
            print("Your command is not valid.")
            continue

    # Function for complete todos
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        # In case user inputs wrong number
        except IndexError:
            print("There is no items with that number.")
    # Exit function
    elif user_action.startswith("exit"):
        exit()
    else:
        print("Command is not valid")

print("Bye!")
