import datetime
from tasks import Task 
from users import User, Owner # NEW IMPORT

class TaskList:
    def __init__(self, owner: Owner):  
        self.owner = owner
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, ix):
        del self.tasks[ix]
        
# added a new method to the TaskList class called get_task which takes an index as an argument and returns the task at that index in the list of tasks. 
# This allows us to easily access a specific task in the list when we want to mark it as completed or change its title, description, or due date.
    def get_task(self, ix):
        return self.tasks[ix]
    
    def view_tasks(self):
        print(f"\nTasks for {self.owner}:") # show owner of the task list when viewing tasks
        for task in self.tasks:
            print(f"Title {task.title}, Description: {task.description}, Due Date: {task.date_due}, Status: {'Completed' if task.completed else 'Not Completed'}")       
# on above line, added description to the print statement to show the description of the task as well when viewing tasks in the list.
    def view_overdue_tasks(self):
        current_date = datetime.datetime.now()
        for task in self.tasks:
            if task.date_due < current_date and not task.completed:
                print(f"Title {task.title}, Due Date: {task.date_due}, Status: {'Completed' if task.completed else 'Not Completed'}")

    