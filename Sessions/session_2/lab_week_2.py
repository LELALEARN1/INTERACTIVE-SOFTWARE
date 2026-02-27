#Section 1: Comparisons and Conditionals
# Comparison operators
is_true = True
is_true = 5 > 4

# Logical operators
age = 25
is_in_age_range = age > 20 and age < 30

#Exercise 3: if - Conditionals
age = 16
#converting age to an integer for calculations
aged = int(age)
age_group = "child"

if aged > 18:
    age_group = "adult"

print(f"The age group is {age_group}")

#Ex 4: if - else Conditionals
wind_speed = 9

if wind_speed < 10:
    print("It is a calm day")
else:
    print("It is a windy day")

#Ex 5: if - elif - else Conditionals
grade = 88

if grade < 50:
    print("You failed")
elif grade < 60:
    print("You passed")
elif grade < 70:
    print("You got a good pass")
else:
    print("You got an excellent pass")

#Ex 6: Summary Tasks
temperature1 = 10
temperature2 = 10

if temperature1 == temperature2:
    print("temperture 1 and tenperature2 are equal")
else:
    print("The 2 temperatures are not equal")

#Section 2 : Python Lists
#Ex 1: Creating a List
integer_list = [1, 2, 3, 4, 5]
string_list = ["apple", "banana", " orange", "grape"]
empty_list = []
list_with_different_types = [1, "two", 3.0, True]

person_1_age = 20
person_2_age = 30
#creating an list based on variables
age_list = [person_1_age, person_2_age]

list_within_a_list = [["red", "green", "blue"], ["yellow", "orange", "purple"]]

#Task: create a list in the variable city_list
city_list = ["Glasgow", "London", "Edinburgh"]

#Ex 2: Accessing a list
second_item = string_list[1] # will store "banana" in the 2nd item
string_list[0:2] # will return ["apple", "banana"]
last_item = string_list[-1] #will store "grape in the last_item

#Ex 3: Modifying a list
string_list[0] = "pear"
string_list.append("orange")
#Task: add the item "Manchester" to the end of the city_list list
city_list.append("Manchester")
print(city_list)

city_list[1] = "Birmingham"
print(city_list)

#Ex 4: Summary Task
#Task: CREATE, ACCESS & MODIFY Lists
colours = ["red", "pink", "orange"]
print(colours)

print(colours[1])
#modify the first element of your list to a new colour of your choice
colours[0] = "gold"
#print the modified list  
print(colours)

#check & print the length of colours list using the
#len() method. this is similar to using the type()
#method from before
print(len(colours))
#use a conditional to check is "red" is in the colours
#list. If yes, print that "Red is in the list"
if "red" in colours:
    print("Red is in the list")
else:
    print("red is not in the list")
#uase slicing to craete a new lsit named 
#selected_colours containing the second and
#third elements from the colours list
selected_colours = colours[1:3]
#print the selected_colours list
print(selected_colours)

#Section 3: Python Loops
i = 0
while i < 5:
    print(i)
    i += 1

#Ex 2: For Loops
for fruit in string_list:
    print(fruit)

#Task: Create a for loop that prints each item
#in the city_list list
for city in city_list:
    print(city)

#Ex 3: 
range(0,5) # will return [0, 1, 2, 3, 4]
range(5) # will return [0, 1, 2, 3, 4]
range(0, 5, 2) # will return [0, 2, 4] because the 
#third parameter is the step size
range(5, 0, -1) #will return [5, 4, 3, 2, 1]

for i in range(5):
    print(i)

for i in range(5):
    if i == 3:
        break
    print(i)

#Task: modify the code above to print the numbers
# 0 through 4, but stop the loop when i is equal to 3

#to continue counting form 0 to 4, but skip the
#number 2, we can do this by using the continue
#keyword inside an if statement like this:
for i in range(5):
    if i == 2:
        continue
    print(i)

#Ex 4: Sumamry Tasks
#Task: Even numbers
#create a list of numbers from 1 to 10
#use a for loop to iterate through the list and  
#only print the even unumbers (Hint: use the
#modulo % operator)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number % 2 == 0:
        print(number)

#Sum of Squares
sum_of_squares = 0
for i in range(6):
    sum_of_squares += i ** 2
    print(sum_of_squares)

#Task: Countdown
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Liftoff!")

#Section 4: Obtaining user input

user_input = input("Enter something: ")
print("You entered: ", user_input)

age = input("How old are you? ")

#Convert the age to an integer
age = int(age)

next_year_age = age + 1
print("Next year, you'll be", next_year_age, "years old.")

#Ex 1: User input Tasks
#Task 1: User Input and Conditional Statements
users_age = input("Enter your age: ")
users_age = int(users_age)
if users_age < 18:
    print("You are a minor.")
elif users_age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.") 

#Task: Temperature Converter
my_string_zero = "Welcome to temperature converter"
print(my_string_zero)
celsius_input = input("Enter a temperature in Celsius: ")
#convert Celsius input to an integer for calculations
celsius = int(celsius_input)
string_one = f"The temperature you have entered is {celsius_input} Celsius."
print(string_one)
degree_f = ((celsius * 2) + 30)
string_two = f"{celsius} Celsius is equivalent to {degree_f} Fahrenheit"
print(string_two)
degree_k = (celsius + 273.15)
string_three = f"{celsius} Celsius is equivalent to {degree_k} Kelvin"
print(string_three)

#Extra task
my_string_zero ="Welcome to Temperature Converter Extra"
print(my_string_zero)
celsius_input = input("Enter a temperature in Celsius:")
celsius = int(celsius_input) # converted to integer
string_selection = input("Would you like to convert to F or K? Enter F or K:")
string_one = f"The temperature you have entered is {celsius} Celsius."
print(string_one)
if string_selection == "F":
    degree_f = ((celsius * 2) + 30)
    string_two = f"{celsius} Celsius is equivalent to {degree_f} Fahrenheit."
    print(string_two)
else:
    degree_k == (celsius + 273.15)
    string_three = f"{celsius} Celsius is equivalent to {degree_k} Kelvin."
    print(string_three)
