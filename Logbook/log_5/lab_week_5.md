# Section 1: Inheritence

## Exercise 1: Simple Inheritence
## Exercise 2: Super() function

```python
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

```

Output when run

```console
The vehicle is moving at 100 km/h
The car is driving at 150 km/h
The electric car is driving at 100 km/h and has a maximum range of 120 km
The petrol car is driving at 150 km/h and has a maximum range of 300 km
The vehicle is moving at 100 km/h
```

### Adding Electric Car and Petrol Car class, page 4


```python
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

```

Output when run

```console

```

## Exercise 3: **kwargs

```python
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
```

output

```console
The electric car is driving at 100 km/h and has a maximum range of 500 km
5
```


