# Basic TaskList Manager
# running fine at Saturday 280226

class TaskList:
    def __init__(self,owner):
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
            print("\nTo_do List Manager")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Quit")

            choice = input("Enter a choice:")
            if choice == "1":
                title = input("Enter a task")
                self.add_task(title)
            
            elif choice == "2":
                self.view_tasks()

            elif choice == "3":
                ix = int(input("Enter index number of task to be removed from list: "))
                self.remove_task(ix)

            elif choice == "4":
                print("Exiting To-Do List Manager")
                break

            else:
                print("Invalid choice. Please try again.")

my_task_list = TaskList("Maggie")
my_task_list.list_options()

