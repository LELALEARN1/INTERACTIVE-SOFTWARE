# Section 2: Python Libraries
# Exercise 1: Adding Dates
# 8 
# Section 2 : Python Libraries
#Exercise 1: Adding Dates                       WORKING SUNDAY 01/03/26
import datetime

class Task:
    def __init__(self, title, completed=False, date_due=datetime.datetime.now()):
        self.title = title
        self.completed = completed
        self.date_created = datetime.datetime.now() 
        self.date_due = date_due

    def __str__(self):
        status = "Completed" if self.completed else "not completed"
        return f"Task {self.title}"
    
    def change_date_due(self, new_date):
        self.date_due = new_date

    def mark_completed(self):
        self.completed = True

    def change_title(self, new_title):
        self.title = new_title

class TaskList:
    def __init__(self, owner):  
        self.owner = owner.upper()
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, ix):
        del self.tasks[ix]

    def view_tasks(self):
        for task in self.tasks:
            print(f"Title {task.title}, Due Date: {task.date_due}, Status: {'Completed' if task.completed else 'Not Completed'}")

    def list_options(self):
        while True:
            print("\nTo_do List Manager")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Mark a task as completed")
            print("5. Change a task title")
            print("6. Change a task due date")
            print("7. Quit")

            choice = input("Enter a choice: ")
            if choice == "1":
                title = input("Enter a task: ")
                input_date = input("Enter a due date for the task (YYYY-MM-DD): ")
                date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d") 
                task = Task(title, completed=False, date_due=date_object)
                self.add_task(task)
            
            elif choice == "2":
                self.view_tasks()

            elif choice == "3":
                ix = int(input("Enter number of task to be removed from list: "))
                self.remove_task(ix -1)  # Adjusting for 0-based index

            elif choice == "4":
                ix = int(input("Enter number of task to be marked as completed: "))
                self.tasks[ix-1].mark_completed() # Adjusting for 0-based index

            elif choice == "5":
                ix = int(input("Enter number of task to be changed: "))
                new_title = input("Enter new title:")
                self.tasks[ix-1].change_title(new_title) # Adjusting for 0-based index

            elif choice == "6":
                ix = int(input("Enter number of task to be changed: "))
                new_date = input("Enter new due date (YYYY-MM-DD): ")
                date_object = datetime.datetime.strptime(new_date, "%Y-%m-%d")
                self.tasks[ix-1].change_date_due(date_object) # Adjusting for 0-based index

            elif choice == "7":
                print("Exiting To-Do List Manager")
                break

            else:
                print("Invalid choice. Please try again.")

my_task_list = TaskList("Maggie")
my_task_list.list_options()
