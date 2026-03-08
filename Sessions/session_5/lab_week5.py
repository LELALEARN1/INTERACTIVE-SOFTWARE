#%% Inheritance Example
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

#%% Super() function example
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
# POLYMORPHISM

class Animal:  
# we omit the __init__ method for brevity  
def move(self, speed):  
print(f"The animal is moving at a speed of {speed}")  
generic_animal = Animal()  
generic_animal.move(20)  




