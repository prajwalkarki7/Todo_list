Task_list={}
def main():
    while True:
        choice = int(input("Enter the choice you want to choose:\n 1. Add\n 2. remove\n 3. set_complete\n 4. Display\n 5. save_task\n 6. load_task\n 7.Exit\n"))
        if choice == 1:
            add_task()
        elif choice == 2:
            remove_task()
        elif choice == 3:
            completed_task()
        elif choice == 4:
            display_task()
        elif choice == 5:
            save_tasks('task.txt')
        elif choice == 6:
            load_tasks('task.txt')
        elif choice==7:
            print("exiting...")    
            break
        else:
            print("Incorrect choice")
def add_task():
    id=int(input("enter the task number:"))
    task= input("enter the task:")
    deadline=input("enter the deadline for the task (give in time like 1,2,3 am/pm):")
    priority=input("enter the priority of the task (top,middle,low):")
    Task_list[id]={'task':task,'deadline':deadline,'priority':priority}
    print("task added successfully!\n")  
def remove_task():
    y=int(input("enter the task id:"))
    if y in Task_list:
        Task_list.pop(y)
        print("task removed successfully\n")
    else:
        print("No task to show\n")
def completed_task():
    z=int(input("enter the id you want to set as complete:"))
    completed=[]
    if z in Task_list:
        completed.append(Task_list[z])
        print(f'task having task_id{z} has been mark as complete\n')
    else:
        print(f"task having task_id{z} not found\n")    
def display_task():
    if not Task_list:
        print("no any task have been found")
    else:
        print("\n Tasks are:")
        for id, details in Task_list.items():
            print(f"Task Number: {id}\n")
            print(f"  task: {details['task']}\n")
            print(f"  deadline: {details['deadline']}\n")
            print(f"  priority: {details['priority']}\n")
            print("-" * 30)  
def save_tasks(filename):
    with open(filename, 'w') as file:
        for id, details in Task_list.items():
            line = f"{id},{details['task']},{details['deadline']},{details['priority']}\n"
            file.write(line)
    print(f"Tasks saved to {filename}.")

def load_tasks(filename):
    global Task_list
    Task_list = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                id_str, task, deadline, priority = line.strip().split(',', 3)
                Task_list[int(id_str)] = {
                    'task': task,
                    'deadline': deadline,
                    'priority': priority
                }
        print(f"Tasks loaded from {filename}.")
    except FileNotFoundError:
        print(f"{filename} not found. Starting with an empty task list.")
    except Exception as e:
        print(f"An error occurred: {e}")
main()

