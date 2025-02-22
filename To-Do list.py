print("   Welcome to Statex TO-DO LIST  ")

RECORD=[]    #list storage

#function to add a task 
def add_task():
    task=input("Add a task to your list: ")
    RECORD.append(task)
    print(f"{task} is successfully Added.")

#function to veiw the tasks
def view_task():
    print("RECORED TASKS")
    if not RECORD:
        print("no tasks in storage ")
    else:
        for index,value in enumerate(RECORD,start=1):
         print(f"{index}){value.capitalize()}")

#function to remove a task
def remove_task(index ):
    if 0<=index <len(RECORD):
        remove_task=RECORD.pop(index)
        print(f"{remove_task} is romeved successfully")
    else:
        print("incoreet numbe")

def show_menu():
    print("\n TASK options ")
    print("1.ADD A TASK")
    print("2.VIEW TASKS")
    print("3.REMOVE A TASKS")
    print("4.EXIT")

while True:
    show_menu()

    choice=input("choose your tasks option:")

    if choice=="1":
        add_task()
    elif choice=="2":
        view_task()
    elif choice=="3":
        view_task()
        index = int(input("Enter task number to remove: ")) - 1
        remove_task(index)
    elif choice=="4":
        print("byeee")
        break
    else:
        print("enter a correct option ")