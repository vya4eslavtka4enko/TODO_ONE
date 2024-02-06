while True:
    user_action=input("Type add, show, edit, complete or exit  :")
    user_action = user_action.strip()
    
    
    if  'add' in user_action or 'new' in user_action:
            if len(user_action) > 4:
                todo = user_action[4:]
            else:
                todo = input("Enter todo: ")+"\n"
            file = open('task.txt','r')
            task = file.readlines()
            file.close()
            task.append(todo)
            file = open('task.txt','w')
            # file.write('\n')
            file.writelines(task)
            file.close()
            
    elif  "show" in user_action:
            file = open("task.txt","r")
            todo = file.readlines()
            file.close()
            for index,item in enumerate(todo):
                row = f"{index+1}-{item}"
                print(row)
                
    elif  "edit" in user_action:
            if len(user_action)>5:
                number_task = int(user_action[5:])-1 
                file = open('task.txt','r')
                task = file.readlines()
                file.close()
            else:
                file = open('task.txt','r')
                task = file.readlines()
                file.close()
                number_task = int(input("Enter the number of task which you want replece "))
                number_task = number_task-1
                print(task[number_task])
            new_task = input("Enter the new task ")
            task[number_task]=new_task+'\n'
            print(task)
            with open('task.txt','w') as file:
                file.writelines(task)

    elif "comlete" in user_action:
            complate_task = int(input("Enter the number of task which you finish "))
            complate_task -=1
            with open('task.txt','r') as file:
                task = file.readlines()
                task.remove(task[complate_task])
                
            file = open("task.txt",'w')
            file.writelines(task)
            print(task)
    elif "exit" in user_action:
        break
    else:
        print("The program not valid ")