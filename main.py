while True:
    user_action=input("Type add, show, edit, complete or exit  :")
    user_action = user_action.strip()
    
    match user_action:
        case "add":
            todo = input("Enter todo: ")+"\n"
            file = open('task.txt','r')
            task = file.readlines()
            file.close()
            task.append(todo)
            file = open('task.txt','w')
            file.write('\n')
            file.writelines(task)
            file.close()
        case "show":
            file = open("task.txt","r")
            todo = file.readlines()
            for index,item in enumerate(todo):
                row = f"{index+1}-{item}"
                print(row)
        case "complate":
            print('User choose complate')