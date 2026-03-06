from task_list import TaskList  
from tasks import Task
import datetime

#  Files readyto start exercise 2.

def propagate_task_list(task_list: TaskList) -> TaskList:  
    """Propagates a task list with some sample tasks.  

    Args: task_list (TaskList): Task list to propagate.  

    Returns: TaskList: The propagated task list.  
    """      
    task_list.add_task(Task("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4)))   
    task_list.add_task(Task("Do laundry", datetime.datetime.now() - datetime.timedelta(days=-2)))   
    task_list.add_task(Task("Clean room", datetime.datetime.now() + datetime.timedelta(days=-1)))   
    task_list.add_task(Task("Do homework", datetime.datetime.now() + datetime.timedelta(days=3)))  
    task_list.add_task(Task("Walk dog", datetime.datetime.now() + datetime.timedelta(days=5)))    
    task_list.add_task(Task("Do dishes", datetime.datetime.now() + datetime.timedelta(days=6)))

    return task_list  

def list_options(task_list):
    #propagate the task list with some sample tasks
    task_list = propagate_task_list(task_list)

    #task_list = propagate_task_list(task_list)

    while True:
    
        print("\nTo_do List Manager")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Mark a task as completed")
        print("5. Edit a task")
        print("6. Change a task due date")
        print("7. Quit")

        choice = input("Enter a choice: ")

        if choice == "1":
            title = input("Enter a task: ")
            input_date = input("Enter a due date for the task (YYYY-MM-DD): ")
            date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d") 
            task = Task(title, completed=False, date_due=date_object)
            task_list.add_task(task)
            
        elif choice == "2":
            task_list.view_tasks()

        elif choice == "3":
            ix = int(input("Enter number of task to be removed from list: "))
            task_list.remove_task(ix -1)  # Adjusting for 0-based index

        elif choice == "4":
            ix = int(input("Enter number of task to be marked as completed: "))
            task_list.tasks[ix-1].mark_completed() # Adjusting for 0-based index
  

        elif choice == "5":
            ix = int(input("Enter number of task to be changed: "))
            new_title = input("Enter new title:")
            task_list.tasks[ix-1].change_title(new_title) # Adjusting for 0-based index
            ch_description = input("Do you want to change the description of the task? (y/n): ")
            if ch_description.lower() == "y":
                new_description = input("Enter new description: ")
                task_list.tasks[ix-1].change_description(new_description) # Adjusting for 0-based index

        elif choice == "6":
            ix = int(input("Enter number of task to be changed: "))
            new_date = input("Enter new due date (YYYY-MM-DD): ")
            date_object = datetime.datetime.strptime(new_date, "%Y-%m-%d")
            task_list.tasks[ix-1].change_date_due(date_object) # Adjusting for 0-based index

        elif choice == "7":
            print("Exiting To-Do List Manager")
            break

        else:
            print("Invalid choice. Please try again.")

def main() -> None:

    owner = input("Enter your name: ")
    task_list = TaskList(owner)

#    task_list = propagate_task_list(task_list) # populate once # add this line back in to populate the task list with some sample tasks if required
    list_options(task_list)

if __name__ == "__main__":  
    main()

