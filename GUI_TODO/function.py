filepath = 'task.txt'

def get_todo():
    with open(filepath,'r') as file:
        task = file.readlines()
    return task


def write_todos(todos_arg):
    with open(filepath,'w') as file:
        file.writelines(todos_arg)