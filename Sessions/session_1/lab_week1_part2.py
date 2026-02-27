#Session 1 Section 2 Python Introduction
#%%
#Exercise 1 task: Variables and Types
x = 10
name = "Alice"
pi = 3.14159

var_1 = True   # Type =
var_2 = 1   # Type
var_3 = 3.14159   # Type
var_4 = "Hello World"   # Type

print(type(var_1))
print(type(var_2))
print(type(var_3))
print(type(var_4))

my_int = 5
my_float = 5.5
my_bool = True

print(my_int)
print(my_float)
print(my_bool)
my_int_float = float(my_int)
my_float_int = int(my_float)
my_bool_int = int(my_bool)

print(type(my_int_float))
print(type(my_float_int))
print(type(my_bool_int))

#%%
#Exercise 2: ARITHMETIC OPERATORS

#Addition
result_addition = 10 + 5
print("Addition: ", result_addition)

#Subtraction
result_subtraction = 20 - 8
print("Subtraction: ", result_subtraction)

#Multiplication
result_multiplication = 6 * 4
print("Multiplication: ", result_multiplication)

#Division
result_division = 15 / 3
print("Division: ", result_division)

#Floor Division
result_floor_division = 17//4
print("Floor Division: ", result_floor_division)

#Modulus
result_modulus = 17 % 4
print("Modulus: ", result_modulus)

#Exponentiation
result_exponentiation = 2 ** 3
print("Exponentiation: ", result_exponentiation)
#Calculating the Average
num1 = 2
num2 = 5
sum = num1 + num2
average = sum / 2
print(average)
#Calculate the area of a triangle 
length = 6
width = 3
area = length * width
print(area)

#Exercise 3: Strings & f-Strings
#Task - Modify Strings
my_string = "This class covers OOP."
print(my_string)
my_uppercase_string = my_string.upper()
print(my_uppercase_string)
my_lowercase_string = my_string.lower()
print(my_lowercase_string)
class_name = "Object Oriented Programming"
my_string = "This class covers " + class_name
print(my_string)

#Task F-Strings, page 6
my_name = "Lesley"
number_of_classes = 3
campus = "Paisley"

my_text = f"My name is {my_name} and I am studying {number_of_classes} in {campus}."
print(my_text)

