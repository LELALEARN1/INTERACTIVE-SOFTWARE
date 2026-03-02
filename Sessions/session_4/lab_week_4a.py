#%%
class TaskList:
    def __init__(self, owner):
        self.owner = owner.upper()
        self.tasks = []

my_task_list = TaskList("John")
print(my_task_list.owner)

# small code change

#%%
class TaskList:
    def __init__(self, owner):
        self.owner = owner.upper()
        self.tasks = []

my_task_list = TaskList("John")
print(my_task_list.owner)

#%%
class TaskList:
    def __init__(self, owner):
        self.owner = owner.upper()
        self.tasks = []

#my_task_list = TaskList("John")
#print(my_task_list.owner)

    def add_task(self, task):
        self.tasks.append(task)
    
    def remove_task(self,ix):
        del self.tasks[ix]
      
    def view_tasks(self):
        for task in self.tasks:
            print(task)
          
    def list_options(self):
        while True:
            print("\nTo-Do List Manager")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove task")
            print("4. Quit")

            choice = input("Enter your choice")
            if choice == "1":
                task = input("Enter a task:")
                self.add_task(task)
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                ix = int(input("Enter the index number of the task to be removed:"))
                self.remove_task(ix)
            elif choice == "4":
                print("Exiting To-Do List Manager")
                break
            else:
                print("Invalid choice. Please re-enter.")
    
#calling the 'Tasklist' Class & passing an argument to the Class and calling the 'list_options' function
my_task_list = TaskList("Alex")
my_task_list.list_options()
        
#%%

#Exercise 3: Testing the Functionality
class TaskList:
    def __init__(self, owner):
        self.owner = owner.upper()
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
    
    def remove_task(self,ix):
        del self.tasks[ix]
      
    def view_tasks(self):
        for task in self.tasks:
            print(task)
          
    def list_options(self):
        while True:
            print("\nTo-Do List Manager")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove task")
            print("4. Quit")

            choice = input("Enter your choice")
            if choice == "1":
                task = input("Enter a task:")
                self.add_task(task)
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                ix = int(input("Enter the index number of the task to be removed:"))
                self.remove_task(ix)
            elif choice == "4":
                print("Exiting To-Do List Manager")
                break
            else:
                print("Invalid choice. Please re-enter.")

my_task_list = TaskList("LYNN")
my_task_list.tasks = ["Do Homework", "Do Laundry", "Go Shopping"]
my_task_list.list_options


#%%
# TUESDAY 240226 
# Exercise 3: Test Functionality (again)

class Tasklist:
    def __init__(self, owner):
        self.owner = owner.upper()
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, ix):
        del self.tasks[ix]

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def list_options(self):
      while True:
        print("\nTo-Do List Manager")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if choice == "1":
          title = input("Enter a task: ")
          self.add_task(task)
        elif choice == "2":
          self.view_tasks()
        elif choice == "3": 
          ix = int(input("Enter the index number of the task to remove:"))
          self.remove_task(ix)
        elif choice == "4": 
          print("Exiting todo list manager")
          break
        else:
          print("Invalid choice. Please re-enter.")

#Testing the FUNCTIONALITY
my_task_list = TaskList("Maggie")
my_task_list.list_options()

#%%
#Exercise 4: COMPOSITION
# TUESDAY 240226 
class Task:
    def __init__(self,title):
        self.title = title

class TaskList:
    def __init__(self,owner):
        self.owner = owner.upper()
        self.tasks = []

    def __str__(self):
        return f"Task: {self.title}"

    def add_task(self, task_title):
        new_title = Task(task_title)
        self.tasks.append(new_task)

    def remove_task(self, ix):
        del self.tasks[ix]

    def view_tasks(self):
        for task in self.tasks:
            print(task.title)

    def list_options(self):
        while True:
                print("\nTo-Do List Manager")
                print("1. Add a Task")
                print("2. View Tasks")
                print("3. Remove a Task")
                print("4. Quit")

                choice = input("Enter your choice: ")
                if choice == "1":
                    title = input("Enter a task: ")
                    task = Task(title)
                    self.add_task(task)

                elif choice == "2":
                    self.view_tasks()

                elif choice == "3":
                    ix = int("Enter index number of task to be removed from list: ")
                    self.remove_task(ix)

                elif choice == "4":
                    print("Exiting To-Do List Manager")
                    break

                else:
                    print("Invalid choice. ")

my_task_list = TaskList("Lynn")
#my_task_list.list_options()

#%%
#Exercise 5: Developing the Task

class Task:
    def __init__(self, title, completed):
        self.title = title
        self.completed = False
        # new Attribute

    def mark_completed(self):
        self.completed = True
    
    def change_title(self, new_title):
        self.title = new_title
    #takes title & changes it into new_title

class TaskList:
    def __init__(self, owner):
        self.owner = owner.upper()
        self.tasks = []

    def __str__(self):
        status = "Completed" if self.completed else "not completed"
        return f"Task: {self.title} {status}"

    def add_task(self, task_title):
        new_title = Task(task_title)
        self.tasks.append(new_task)

    def remove_task(self, ix):
        del self.tasks[ix]

    def view_tasks(self):
        for task in self.tasks:
            print(task.title)

    def list_options(self):
        while True:
                print("\nTo-Do List Manager")
                print("1. Add a Task")
                print("2. View Tasks")
                print("3. Remove a Task")
                print("4. Mark a task as completed")
                print("5. Change a task title")
                print("6. Quit")

                choice = input("Enter your choice: ")
                if choice == "1":
                    title = input("Enter a task: ")
                    task = Task(title)
                    self.add_task(task)

                elif choice == "2":
                    self.view_tasks()

                elif choice == "3":
                    ix = input("Enter index number of task to be removed from list: ")
                    del self.tasks[ix]

                elif choice == "4":
                    ix = input("Enter the index number of the task to be marked as completed")
                    self.tasks[ix].mark_completed

                elif choice == "5":
                    ix = input("Enter the index number of the task to be changed")
                    new_title = input("Enter the new title of the task to be changed")
                    self.tasks[ix].change_title(new_title)

                elif choice == "6":
                    print("Exiting To-Do List Manager")
                    break

                else:
                    print("Invalid choice. ")

my_task_list = TaskList("Lynn")
my_task_list.list_options()
#%%

#%%
import datetime

class Task:
    def __init__(self, title, completed, date_created, date_due):
        self.title = title
        self.completed = False
        self.date_created = datetime.datetime.now()
        self.date_due = date_due

    def change_date_due(self, new_due_date):
        self.date_due = new_due_date
    
    def mark_completed(self):
        self.completed = True
    
    def change_title(self, new_title):
        self.title = new_title
    #takes title & changes it into new_title

class TaskList:
    def __init__(self, owner):
        self.owner = owner.upper()
        self.tasks = []

    def __str__(self):
        status = "Completed" if self.completed else "not completed"
        return f"Task: {self.title} {status}"

    def add_task(self, task_title):
        new_title = Task(task_title)
        self.tasks.append(new_task)

    def remove_task(self, ix):
        del self.tasks[ix]

    def view_tasks(self):
        for task in self.tasks:
            print(task.title)

    def list_options(self):
        while True:
                print("\nTo-Do List Manager")
                print("1. Add a Task")
                print("2. View Tasks")
                print("3. Remove a Task")
                print("4. Mark a task as completed")
                print("5. Change a task title")
                print("6. Change a due date of a task")
                print("7. Quit")

                choice = input("Enter your choice: ")
                if choice == "1":
                    input_date = input("Enter a due date for the task (YY-MM-DD): ")
                    date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")
                    title = input("Enter a task: ")
                    task = Task(title, date_object)
                    self.add_task(task)

                elif choice == "2":
                    self.view_tasks()

                elif choice == "3":
                    ix = input("Enter index number of task to be removed from list: ")
                    del self.tasks[ix]

                elif choice == "4":
                    ix = input("Enter the index number of the task to be marked as completed")
                    self.tasks[ix].mark_completed

                elif choice == "5":
                    ix = input("Enter the index number of the task to be changed")
                    new_title = input("Enter the new title of the task to be changed")
                    self.tasks[ix].change_title(new_title)

                elif choice == "6":
                    ix = input("Enter the index number of the task to change due date")
                    input_date = input("Enter a new due date for the task (YY-MM-DD): ")
                    date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")
                    self.tasks[ix].change_date_due(date_object)

                elif choice == "7":
                    print("Exiting To-Do List Manager")
                    break

                else:
                    print("Invalid choice. ")

my_task_list = TaskList("Lynn")
my_task_list.list_options()
#%%
