while True:
    user_action=input("Type add, show, edit, complete or exit  :")
    user_action = user_action.strip()
    
    match user_action:
        case "add":
            todo = input("Enter todo: ")+"\n"
            file = open('task.txt','r')
            task = file.readlines()
            task.append(todo)
            file = open('task.txt','w')
            file.write('\n')
            file.writelines(task)
            file.close()
        case "show":
            print("User choose show")
        case "complate":
            print('User choose complate')