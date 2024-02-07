def get_todo():
    with open("task.txt",'r') as file:
        task = file.readlines()
    return task


def write_todos(filepath, todos_arg):
    with open(filepath,'w') as file:
        file.writelines(todos_arg)

while True:
    user_action=input("Type add, show, edit, complete or exit  :")
    user_action = user_action.strip()
    
    
    if  user_action.startswith('add') :
            if len(user_action) > 4:
                todo = user_action[4:]
            else:
                todo = input("Enter todo: ")+"\n"
            task = get_todo()
            task.append('\n')
            task.append(todo)
            write_todos("task.txt",task)
            
    elif  user_action.startswith('show'):
            todo = get_todo()
            for index,item in enumerate(todo):
                row = f"{index+1}-{item}"
                print(row)
                
    elif  user_action.startswith('edit'):
        try:
            if len(user_action)>5:
                number_task = int(user_action[5:])-1 
                task = get_todo()
            else:
                task = get_todo()
                number_task = int(input("Enter the number of task which you want replece "))
                number_task = number_task-1
                print(task[number_task])
            new_task = input("Enter the new task ")
            task[number_task]=new_task+'\n'
            print(task)
            write_todos('task.txt',task)
        except ValueError:
            print('Your command not valid')
            continue
    elif user_action.startswith('complete'):
        try:
            complate_task = int(input("Enter the number of task which you finish "))
            complate_task -=1
            task = get_todo()
            task.remove(task[complate_task])
                
            write_todos("task.txt",task)
        except IndexError:
            print("There is no item with that number ")
    elif "exit" in user_action:
        break
    else:
        print("The program not valid ")