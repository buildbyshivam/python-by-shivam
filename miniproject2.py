
tasks = []
while True:
    print("\n..to do list ")
    print("1.add.task")
    print("2.view task")
    print("3.delete task")
    print("4.exit")
    choice=input("enter the task number")

    if choice =="1":
        task = input("enter the task which you want to add")
        tasks.append(task)
        print("task is added!")
    elif choice=="2":
        if len(tasks)==0:
            print("no task")
        else:
            print("\n tasks")
            for i,task in enumerate(tasks):
                print(f"{i+1}.{task}")
    elif choice == "3":
        for i ,task in enumerate(tasks):
            print(f"{i+1}.{tasks}")
            num = int(input("enetr the value you want to delete"))
            if 0<num<=len(tasks):
                tasks.pop(num-1)
                print("task deleted")
            else:
                print("invalid statement")
    elif choice == 4:
        print("goodbye exit")

    else:
        print("invalid statement")


















