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