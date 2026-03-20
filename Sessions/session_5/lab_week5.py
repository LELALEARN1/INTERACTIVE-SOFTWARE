#%% 
# Inheritance Example
# added the init method to the Car class, which calls the init method of the Vehicle class using super() to initialize the common 
# attributes (colour, weight, max_speed) & then initializes the specific attribute form_factor for the Car class.
# also added a move method to the Car class to overrides= the move method of the Vehicle class, givinging specific behaviour for when a car is moving.

# super() function is used to call the init method of the parent class (Vehicle) from the child class (Car) to ensure that the common attributes are properly initialized when creating an instance of the Car class.
 
class Vehicle: 
    def __init__(self, colour, weight, max_speed, max_range=None):  
      self.colour = colour   
      self.weight = weight  
      self.max_speed = max_speed  
      self.max_range = max_range 
    def move(self, speed):
      print(f"The vehicle is moving at {speed} km/h")  

class Car(Vehicle):      
   def __init__(self, colour, weight, max_speed, form_factor, max_range=None):  
       super().__init__(colour, weight, max_speed, max_range)      
       self.form_factor = form_factor  
 
   def move(self, speed):  
       print(f"The car is driving at {speed} km/h")

class Electric(Car):      
   def __init__(self, colour, weight, max_speed, form_factor, battery_capacity, max_range=None):  
       super().__init__(colour, weight, max_speed, form_factor, max_range)  
       self.battery_capacity = battery_capacity  
 
   def move(self, speed):  
       print(f"The electric car is driving at {speed} km/h and has a maximum range of {self.max_range} km")  
 
class Petrol(Car):      
   def __init__(self, colour, weight, max_speed, form_factor, fuel_capacity, max_range=None):  
    super().__init__(colour, weight, max_speed, form_factor, max_range)     
    self.fuel_capacity = fuel_capacity  
 
   def move(self, speed):  
       print(f"The petrol car is driving at {speed} km/h and has a maximum range of {self.max_range} km") 

generic_vehicle = Vehicle("red", 1000, 200)  
generic_vehicle.move(100)  
 
car = Car("blue", 1500, 250, "SUV")  
car.move(150) 

electric_car = Electric("green", 1200, 200, "Hatchback", 100, 120)
electric_car.move(100)  
 
petrol_car = Petrol("red", 1500, 250, "SUV", 50, 300)  
petrol_car.move(150)  
 
generic_vehicle = Vehicle("red", 1000, 200) 
generic_vehicle.move(100)


#%%
# Super() function example
class Vehicle:      
     def __init__(self, colour, weight, max_speed):  
        self.colour = colour              
        self.weight = weight          
        self.max_speed = max_speed  
     def move(self, speed):  
        print(f"The vehicle is moving at {speed} km/h")

class Car(Vehicle):      
   def __init__(self, colour, weight, max_speed, form_factor):  
       super().__init__(colour, weight, max_speed)  
       self.form_factor = form_factor  
  
   def move(self, speed):  
       print(f"The car is driving at {speed} km/h")

#%% 
# ***kwargs example
# added the **kwargs parameter to the init method of the Car class, allowing additional keyword arguments 
# to be passed when creating an instance of the Car class.
# allowing greater flexibility in the Car class, because it can now accept additional attributes 
# that are not totally defined in the Car class but are still relevant  Vehicle class 
# or other subclasses which might inherit from Vehicle.

class Vehicle: 
    def __init__(self, colour, weight, max_speed, max_range=None):
      self.colour = colour   
      self.weight = weight  
      self.max_speed = max_speed  
      self.max_range = max_range 

    def move(self, speed):
      print(f"The vehicle is moving at {speed} km/h")  

class Car(Vehicle):      
   def __init__(self, colour, weight, max_speed, form_factor, **kwargs):  
       super().__init__(colour, weight, max_speed, **kwargs)      
       self.form_factor = form_factor  
 
   def move(self, speed):  
       print(f"The car is driving at {speed} km/h")

class Electric(Car):      
   def __init__(self, colour, weight, max_speed, form_factor, battery_capacity, **kwargs):  
       super().__init__(colour, weight, max_speed, form_factor, **kwargs)  
       self.battery_capacity = battery_capacity  
 
   def move(self, speed):  
       print(f"The electric car is driving at {speed} km/h and has a maximum range of {self.max_range} km")  
 
class Petrol(Car):      
   def __init__(self, colour, weight, max_speed, form_factor, fuel_capacity, **kwargs):  
    super().__init__(colour, weight, max_speed, form_factor, **kwargs)     
    self.fuel_capacity = fuel_capacity  
 
   def move(self, speed):  
       print(f"The petrol car is driving at {speed} km/h and has a maximum range of {self.max_range} km") 
              
generic_vehicle = Vehicle("red", 1000, 200)  
generic_vehicle.move(100)  
 
car = Car("blue", 1500, 250, "SUV")  
car.move(150) 

electric_car = Electric("green", 1200, 200, "Hatchback", 100, max_range=120)
electric_car.move(100)
 
petrol_car = Petrol("red", 1500, 250, "SUV", 50, max_range=300)  
petrol_car.move(150)  

generic_vehicle = Vehicle("red", 1000, 200) 
generic_vehicle.move(100)

#%%
class Vehicle: 
    def __init__(self, colour, weight, max_speed, max_range=None, seats=None):  
      self.colour = colour   
      self.weight = weight  
      self.max_speed = max_speed  
      self.max_range = max_range 
      self.seats = seats

    def move(self, speed):
      print(f"The vehicle is moving at {speed} km/h")  

class Car(Vehicle):      
   def __init__(self, colour, weight, max_speed, form_factor, **kwargs):  
       super().__init__(colour, weight, max_speed, **kwargs)      
       self.form_factor = form_factor  
 
   def move(self, speed):  
       print(f"The car is driving at {speed} km/h")

class Electric(Car):      
   def __init__(self, colour, weight, max_speed, form_factor, battery_capacity, **kwargs):  
       super().__init__(colour, weight, max_speed, form_factor, **kwargs)  
       self.battery_capacity = battery_capacity  
 
   def move(self, speed):  
       print(f"The electric car is driving at {speed} km/h and has a maximum range of {self.max_range} km")  
 
class Petrol(Car):      
   def __init__(self, colour, weight, max_speed, form_factor, fuel_capacity, **kwargs):  
    super().__init__(colour, weight, max_speed, form_factor, **kwargs)     
    self.fuel_capacity = fuel_capacity  
 
   def move(self, speed):  
       print(f"The petrol car is driving at {speed} km/h and has a maximum range of {self.max_range} km") 

generic_electric_car = Electric("red", 1000, 200, "SUV", 100, max_range=500, seats=5)
generic_electric_car.move(100)
print(generic_electric_car.seats)
                
# generic_vehicle = Vehicle("red", 1000, 200)  
# generic_vehicle.move(100)  
 
# car = Car("blue", 1500, 250, "SUV")  
# car.move(150) 

# electric_car = Electric("green", 1200, 200, "Hatchback", 100, max_range=120)
# electric_car.move(100)
 
# petrol_car = Petrol("red", 1500, 250, "SUV", 50, max_range=300)  
# petrol_car.move(150)  
 
# generic_vehicle = Vehicle("red", 1000, 200) 
# generic_vehicle.move(100)

#%%
# with propeller_count and engine_count
class Vehicle: 
    def __init__(self, colour, weight, max_speed, max_range=None, seats=None):  
      self.colour = colour   
      self.weight = weight  
      self.max_speed = max_speed  
      self.max_range = max_range 
      self.seats = seats

    def move(self, speed):
      print(f"The vehicle is moving at {speed} km/h")  

class Plane(Vehicle):      
   def __init__(self, colour, weight, max_speed, max_range=None, seats=None, wing_span=None):  
       super().__init__(colour, weight, max_speed, max_range, seats)  
       self.wing_span = wing_span 
 
   def move(self, speed):  
       print(f"The plane is flying at {speed} km/h and has a maximum range of {self.max_range} km")

class PropellerPlane(Plane):
    def __init__(self, colour, weight, max_speed, max_range=None, seats=None, wing_span=None, propeller_diameter=None, propeller_count=None):
        super().__init__(colour, weight, max_speed, max_range, seats, wing_span)
        self.propeller_diameter = propeller_diameter
        self.propeller_count = propeller_count

    def move(self, speed):
        print(f"The propeller plane is flying at {speed} km/h and has a maximum range of {self.max_range} km with {self.propeller_count} propellers")   

class JetPlane(Plane):
    def __init__(self, colour, weight, max_speed, max_range=None, seats=None, wing_span=None, engine_thrust=None, engine_count=None):
        super().__init__(colour, weight, max_speed, max_range, seats, wing_span)
        self.engine_thrust = engine_thrust
        self.engine_count = engine_count

    def move(self, speed):
        print(f"The jet plane is flying at {speed} km/h and has a maximum range of {self.max_range} km with {self.engine_count} engines")

class Car(Vehicle):      
   def __init__(self, colour, weight, max_speed, form_factor, **kwargs):  
       super().__init__(colour, weight, max_speed, **kwargs)      
       self.form_factor = form_factor  
 
   def move(self, speed):  
       print(f"The car is driving at {speed} km/h")

class Electric(Car):      
   def __init__(self, colour, weight, max_speed, form_factor, battery_capacity, **kwargs):  
       super().__init__(colour, weight, max_speed, form_factor, **kwargs)  
       self.battery_capacity = battery_capacity  
 
   def move(self, speed):  
       print(f"The electric car is driving at {speed} km/h and has a maximum range of {self.max_range} km")  
 
class Petrol(Car):      
   def __init__(self, colour, weight, max_speed, form_factor, fuel_capacity, **kwargs):  
    super().__init__(colour, weight, max_speed, form_factor, **kwargs)     
    self.fuel_capacity = fuel_capacity  
 
   def move(self, speed):  
       print(f"The petrol car is driving at {speed} km/h and has a maximum range of {self.max_range} km") 

# Vehicle
vehicle = Vehicle("white", 1200, 180)
vehicle.move(80)
print(vehicle.colour, vehicle.weight, vehicle.max_speed)

# Plane
plane = Plane("silver", 8000, 900, max_range=5000, seats=180, wing_span=35)
plane.move(700)
print(plane.wing_span, plane.seats)

# PropellerPlane
prop_plane = PropellerPlane("blue", 4000, 500, max_range=2000, seats=40,
                            wing_span=20, propeller_diameter=3,
                            propeller_count=2)
prop_plane.move(350)
print(prop_plane.propeller_count, prop_plane.propeller_diameter)

# JetPlane
jet_plane = JetPlane("white", 10000, 950, max_range=6000, seats=220,
                     wing_span=40, engine_thrust=120000, engine_count=2)
jet_plane.move(850)
print(jet_plane.engine_count, jet_plane.engine_thrust)

# Car
car = Car("black", 1500, 220, "Sedan", seats=5)
car.move(100)
print(car.form_factor, car.seats)

# Electric car
electric_car = Electric("red", 1800, 200, "SUV", 100, max_range=500, seats=5)
electric_car.move(120)
print(electric_car.battery_capacity, electric_car.max_range)

# Petrol car
petrol_car = Petrol("blue", 1700, 230, "Coupe", 60, max_range=650, seats=4)
petrol_car.move(140)
print(petrol_car.fuel_capacity, petrol_car.max_range)

#%%
# without propeller_count and engine_count

class Vehicle: 
    def __init__(self, colour, weight, max_speed, max_range=None, seats=None):  
      self.colour = colour   
      self.weight = weight  
      self.max_speed = max_speed  
      self.max_range = max_range 
      self.seats = seats

    def move(self, speed):
      print(f"The vehicle is moving at {speed} km/h")  

class Plane(Vehicle):      
   def __init__(self, colour, weight, max_speed, max_range=None, seats=None, wing_span=None):  
       super().__init__(colour, weight, max_speed, max_range, seats)  
       self.wing_span = wing_span 
 
   def move(self, speed):  
       print(f"The plane is flying at {speed} km/h and has a maximum range of {self.max_range} km")

class PropellerPlane(Plane):
    def __init__(self, colour, weight, max_speed, max_range=None, seats=None, wing_span=None, propeller_diameter=None):       
        super().__init__(colour, weight, max_speed, max_range, seats, wing_span)
        self.propeller_diameter = propeller_diameter

    def move(self, speed):
        print(f"The propeller plane is flying at {speed} km/h and has a maximum range of {self.max_range} km with propellers of diameter {self.propeller_diameter} m")   

class JetPlane(Plane):
    def __init__(self, colour, weight, max_speed, max_range=None, seats=None, wing_span=None, engine_thrust=None):
        super().__init__(colour, weight, max_speed, max_range, seats, wing_span)
        self.engine_thrust = engine_thrust

    def move(self, speed):
        print(f"The jet plane is flying at {speed} km/h and has a maximum range of {self.max_range} km with engines producing {self.engine_thrust} N of thrust")

class Car(Vehicle):      
   def __init__(self, colour, weight, max_speed, form_factor, **kwargs):  
       super().__init__(colour, weight, max_speed, **kwargs)      
       self.form_factor = form_factor  
 
   def move(self, speed):  
       print(f"The car is driving at {speed} km/h")

class Electric(Car):      
   def __init__(self, colour, weight, max_speed, form_factor, battery_capacity, **kwargs):  
       super().__init__(colour, weight, max_speed, form_factor, **kwargs)  
       self.battery_capacity = battery_capacity  
 
   def move(self, speed):  
       print(f"The electric car is driving at {speed} km/h and has a maximum range of {self.max_range} km")  
 
class Petrol(Car):      
   def __init__(self, colour, weight, max_speed, form_factor, fuel_capacity, **kwargs):  
    super().__init__(colour, weight, max_speed, form_factor, **kwargs)     
    self.fuel_capacity = fuel_capacity  
 
   def move(self, speed):  
       print(f"The petrol car is driving at {speed} km/h and has a maximum range of {self.max_range} km") 

# Vehicle
vehicle = Vehicle("white", 1200, 180)
vehicle.move(80)
print(vehicle.colour, vehicle.weight, vehicle.max_speed)

# Plane
plane = Plane("silver", 8000, 900, max_range=5000, seats=180, wing_span=35)
plane.move(700)
print(plane.wing_span, plane.seats)

# PropellerPlane
prop_plane = PropellerPlane("blue", 4000, 500, max_range=2000, seats=40,
                            wing_span=20, propeller_diameter=3)
prop_plane.move(350)
print(prop_plane.propeller_diameter)

# JetPlane
jet_plane = JetPlane("white", 10000, 950, max_range=6000, seats=220,
                     wing_span=40, engine_thrust=120000)
jet_plane.move(850)
print(jet_plane.engine_thrust)

# Car
car = Car("black", 1500, 220, "Sedan", seats=5)
car.move(100)
print(car.form_factor, car.seats)

# Electric car
electric_car = Electric("red", 1800, 200, "SUV", 100, max_range=500, seats=5)
electric_car.move(120)
print(electric_car.battery_capacity, electric_car.max_range)

# Petrol car
petrol_car = Petrol("blue", 1700, 230, "Coupe", 60, max_range=650, seats=4)
petrol_car.move(140)
print(petrol_car.fuel_capacity, petrol_car.max_range)

# TESTING CONFIRMS THAT THE CODE WORKS WITHOUT propeller_count and engine_count
# and tests that: 
# Inheritance works correctly with the new attributes and methods in the PropellerPlane and JetPlane classes.
# ie Electric and Petrol inherit from Car, which inherits from Vehicle, and PropellerPlane and JetPlane inherit from Plane, which inherits from Vehicle.
# & tests that ATTRIBUTES propagate correctly through the inheritance hierarchy, allowing for the creation of instances with the appropriate attributes and methods.
# max_range passes through **kwargs and is accessible in the move method of PropellerPlane and JetPlane, demonstrating that the attributes are correctly propagated 
# through the inheritance hierarchy.
# and tests that MTHOD overriding works correctly, allowing for the specific behavior of the move method in each class while still maintaining 
# the overall structure of the inheritance hierarchy.
# and tests that METHOD overriding works correctly:
# each subclass has its own move() Method that overrides the move() method of the Vehicle class, allowing for specific behavior for each type of 
# vehicle while still maintaining the overall structure of the inheritance hierarchy.
# and tests that the code is flexible and can be easily extended to include additional types of vehicles or attributes without requiring significant 
# changes to the existing codebase.

#%% 
# adding CLASS FlyingCar 
# that inherits from both Car and Plane, demonstrating multiple inheritance and the ability to combine attributes and methods from both parent classes.
# The FlyingCar class can have its own unique attributes and methods, while still being able to utilize the functionality of both the Car and Plane classes.
# This allows for greater flexibility and code reuse, as the FlyingCar class can leverage the existing functionality of both parent classes while also adding 
# its own specific features.

class Vehicle: 
    def __init__(self, colour, weight, max_speed, max_range=None, seats=None):  
      self.colour = colour   
      self.weight = weight  
      self.max_speed = max_speed  
      self.max_range = max_range 
      self.seats = seats

    def move(self, speed):
      print(f"The vehicle is moving at {speed} km/h")  

class Plane(Vehicle):      
   def __init__(self, colour, weight, max_speed, max_range=None, seats=None, wing_span=None):  
       super().__init__(colour, weight, max_speed, max_range, seats)  
       self.wing_span = wing_span 
 
   def move(self, speed):  
       print(f"The plane is flying at {speed} km/h and has a maximum range of {self.max_range} km")

class PropellerPlane(Plane):
    def __init__(self, colour, weight, max_speed, max_range=None, seats=None, wing_span=None, propeller_diameter=None):       
        super().__init__(colour, weight, max_speed, max_range, seats, wing_span)
        self.propeller_diameter = propeller_diameter

    def move(self, speed):
        print(f"The propeller plane is flying at {speed} km/h and has a maximum range of {self.max_range} km with propellers of diameter {self.propeller_diameter} m")   

class JetPlane(Plane):
    def __init__(self, colour, weight, max_speed, max_range=None, seats=None, wing_span=None, engine_thrust=None):
        super().__init__(colour, weight, max_speed, max_range, seats, wing_span)
        self.engine_thrust = engine_thrust

    def move(self, speed):
        print(f"The jet plane is flying at {speed} km/h and has a maximum range of {self.max_range} km with engines producing {self.engine_thrust} N of thrust")

class Car(Vehicle):      
   def __init__(self, colour, weight, max_speed, form_factor, **kwargs):  
       super().__init__(colour, weight, max_speed, **kwargs)      
       self.form_factor = form_factor  
 
   def move(self, speed):  
       print(f"The car is driving at {speed} km/h")

class Electric(Car):      
   def __init__(self, colour, weight, max_speed, form_factor, battery_capacity, **kwargs):  
       super().__init__(colour, weight, max_speed, form_factor, **kwargs)  
       self.battery_capacity = battery_capacity  
 
   def move(self, speed):  
       print(f"The electric car is driving at {speed} km/h and has a maximum range of {self.max_range} km")  
 
class Petrol(Car):      
   def __init__(self, colour, weight, max_speed, form_factor, fuel_capacity, **kwargs):  
    super().__init__(colour, weight, max_speed, form_factor, **kwargs)     
    self.fuel_capacity = fuel_capacity  
 
   def move(self, speed):  
       print(f"The petrol car is driving at {speed} km/h and has a maximum range of {self.max_range} km") 

class FlyingCar(Car, Plane):  
    def __init__(self, colour, weight, max_speed, form_factor, wing_span, **kwargs):   
        super().__init__(colour=colour, weight=weight, max_speed=max_speed, form_factor=form_factor, wing_span=wing_span, **kwargs)  
 

    def move(self, speed):  
        print(f"The flying car is driving or flying at {speed} km/h")

# generic_flying_car = FlyingCar("red", 1000, 200, "SUV", 30, seats=5) 
# generic_flying_car.move(100) 
# print(generic_flying_car.seats, generic_flying_car.wing_span, generic_flying_car.form_factor) 

generic_flying_car_2 = FlyingCar(colour="red", weight=1000, max_speed=200, 
form_factor="SUV", wing_span=30, seats=5)  
generic_flying_car_2.move(100) 

# %%
# POLYMORPHISM page 10 lab WK5 080326
# Polymorphism lets us use a single interface to represent different
# types of objects, helping code to be written which can work with objects of different classes in a uniform way.

class Animal:  
# we omit the __init__ method for brevity  
    def move(self, speed):  
        print(f"The animal is moving at a speed of {speed}")  
generic_animal = Animal()  
generic_animal.move(20)  

#%%
# ToDO:
# 6. RECURRING TASKS page 11 lab WK6 080326

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

# Adding the code for Recurring task Class to the existing Tasks module (copied from tasks.py) as follows:
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
 
        super().__init__(title, date_due)    
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
# this is a timedela object which shows how often the task should be repeated
# have also added a new attribute called repeated_dates, which is a list that will keep a record of the dates on which the task was completed.
# have also added a new method called _compute_next_due_date, which calculates the next due date for the recurring task based on the current 
# due date and the specified interval.
# have also overridden the str method to provide a string representation of the recurring task, including its title, creation date, due date,
# completion history, and interval.

#%%
# adjusting   main.py (copied from main.py) to include the RecurringTask class as follows:

from Sessions.session_4.ToDoApp import task_list
from task_list import TaskList  
from tasks import Task, RecurringTask
import datetime

# Files readyto start exercise 2;
# no this is copied from exercise 2 to do WK6 lab on recurring tasks, with the addition of the RecurringTask class and some adjustments to the list_options function to handle recurring tasks.

def propagate_task_list(task_list: TaskList) -> TaskList:  
    """Propagates a task list with some sample tasks.  

    Args: task_list (TaskList): Task list to propagate.  

    Returns: TaskList: The propagated task list.  
    """      
                 
# sample recurring task      
    r_task = RecurringTask("Go to the gym", datetime.datetime.now(), 
    datetime.timedelta(days=7))  
# propagate the recurring task with some completed dates    
    r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=7))  
    r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=14))  
    r_task.completed_dates.append(datetime.datetime.now()- datetime.timedelta(days=22))      
    r_task.date_created = datetime.datetime.now() - datetime.timedelta(days=28)  

    task_list.add_task(r_task) 

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
            '''Asked the user to specify whether the task is a regular task or a recurring task. 
            If the user selects recurring task, they are prompted to enter the interval (interval_days) in days 
            for the recurring task. Based on the user's input, either a regular Task or a RecurringTask 
            is created and added to the task list.'''
            task_type = input("Enter task type (1 for regular, 2 for recurring): ")
            input_date = input("Enter a due date for the task (YYYY-MM-DD): ")
            date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")
            
            if task_type == "2":
                interval_days = int(input("Enter interval in days: "))
                interval = datetime.timedelta(days=interval_days) 
                ''' Create a RecurringTask if the user selects recurring task, otherwise create a regular Task& add it to the list. '''
                task = RecurringTask(title, completed=False, date_due=date_object, interval=interval)
                task_list.add_task(task)
            else:
                '''  changed the conditional that if it is a normal task, create a Task object & add it to the list. '''
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
            print("Overdue Tasks:")
            task_list.view_overdue_tasks()

        elif choice == "8":
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

#%%




