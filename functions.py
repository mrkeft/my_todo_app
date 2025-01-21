def get_todos(filepath='todos.txt'):
    """ You can write documentation of your code like this.
    It is used in larger programs
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(local_todos, loc_filepath='todos.txt'):
    """ Write a todo item in the text file."""
    with open(loc_filepath, 'w') as file:
        file.writelines(local_todos)


if __name__ == "__main__":
    print("hello from functions")
    print("Just to test again")