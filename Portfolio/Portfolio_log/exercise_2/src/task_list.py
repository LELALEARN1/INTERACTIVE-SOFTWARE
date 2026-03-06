import datetime
from tasks import Task 

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
            print(f"Title {task.title}, Due Date: {task.date_due}, Status: {'Completed' if task.completed else 'Not Completed'} - Description: {task.description}")


