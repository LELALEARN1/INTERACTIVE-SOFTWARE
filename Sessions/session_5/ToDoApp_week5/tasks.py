# ToDO:
# 6. RECURRING TASKS page 11 lab WK6 

import datetime

class Task:
    def __init__(self, title, completed=False, date_due=datetime.datetime.now(), description = ""):
        self.title = title
        self.completed = completed
        self.date_created = datetime.datetime.now() 
        self.date_due = date_due
        self.description = description

    def __str__(self):
        status = "Completed" if self.completed else "not completed"
        return f"Task: {self.title} - Status: {status} - Due: {self.date_due} - Description: {self.description}"
    
    def change_description(self, new_description):
        self.description = new_description 

    def change_date_due(self, new_date):
        self.date_due = new_date

    def mark_completed(self):
        self.completed = True

    def change_title(self, new_title):
        self.title = new_title

# Adding the code for Recurring task Class to the existing Tasks module from WK6 Lab (copied from tasks.py) as follows:
class RecurringTask(Task):  
    """Represents a recurring task in a to-do list.  
  
    Args:  
        Task (Task): The task to be repeated.  
    """       
 
    def __init__(self, title: str, date_due: datetime.datetime, 
interval: datetime.timedelta):  
        """Creates a new recurring task.  
  
        Args:  
            title (str): Title of the task.             
            date_due (datetime.datetime): Due date of the 
task. 
            interval (datetime.timedelta): Interval between each 
repetition.  
        """          
 
        super().__init__(title, date_due=date_due)    
        self.interval = interval  
        self.completed_dates : list[datetime.datetime] = []  
        # list of datetime.datetime objects  
  
    def _compute_next_due_date(self) -> datetime.datetime:  
        """Computes the next due date of the task.  
  
        Returns:  
            datetime.datetime: The next due date of the task.  
        """          
        return self.date_due + self.interval  
 
    def __str__(self) -> str:  
        return f"{self.title} - Recurring (created: {self.date_created}, due: {self.date_due}, completed: {self.completed_dates}, interval: {self.interval})"  

# have added the interval attribute to the __init__ method 
# this is a timedelta object which shows how often the task should be repeated
# have also added a new attribute called repeated_dates, which is a list that will keep a record of the dates on which the task was completed.
# have also added a new method called _compute_next_due_date, which calculates the next due date for the recurring task based on the current 
# due date and the specified interval.
# have also overridden the __str__ method to provide a string representation of the recurring task, including its title, creation date, due date,
# completion history, and interval.

