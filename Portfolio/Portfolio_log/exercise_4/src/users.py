# adding a new class to represent users of the ToDo app, including an Owner subclass that inherits from User. This will allow us to manage user information and potentially implement features specific to the owner of the task list in the future.
# The User class has attributes for the user's name and email, and a __str__ method to provide a string representation of the user. The Owner subclass inherits from User and can be used to represent the owner of the task list, allowing for potential future functionality specific to the owner.
# The User class has an __init__ method that initializes the name and email attributes, and a __str__ method that returns a string representation of the user. 
# I have also added an Owner subclass that inherits from User, which can be used to represent the owner of the task list. The Owner class has its own __str__ method to provide a string representation specific to the owner.

# still to modify the TaskList class (in the task_list.py file) to include an owner attribute that is an instance of the Owner class, and to update the relevant methods to handle the owner information appropriately.


class User:
    def __init__(self, name):
        self.name = name
        self.email = self.email

    def __str__(self):
        return f"User: {self.name}, Email: {self.email}"
    
class Owner(User):
    def __init__(self, name, email):
            super().__init__(name)

    def __str__(self):
        return f"Owner: {self.name}, Email: {self.email}"


    