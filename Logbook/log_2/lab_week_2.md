- [Section 1: Comparisons and Conditionals](#section-1-comparisons-and-conditionals)
  - [Exercise 1](#exercise-1)
  - [Exercise 2](#exercise-2)
  - [Exercise 3](#exercise-3)
  - [Exercise 4](#exercise-4)
  - [Exercise 5](#exercise-5)
  - [Exercise 6](#exercise-6)
- [Section 2 : Python Lists](#section-2--python-lists)
  - [Ex 1: Creating a List](#ex-1-creating-a-list)
  - [Ex 2: Accessingn a List](#ex-2-accessingn-a-list)
  - [Ex 3: Modifying a List](#ex-3-modifying-a-list)
  - [Ex 4: Summary Task](#ex-4-summary-task)
  - [Task: CREATE, ACCESS \& MODIFY Lists](#task-create-access--modify-lists)
- [Section 3: Python Loops](#section-3-python-loops)
  - [Exercise 1: While Loops](#exercise-1-while-loops)
  - [Exercise 2: For Loops](#exercise-2-for-loops)
  - [Exercise 3: Loop keywords: range, break and continue](#exercise-3-loop-keywords-range-break-and-continue)
- [Exercise 4: Summary Tasks](#exercise-4-summary-tasks)
  - [Task: Even numbers](#task-even-numbers)
- [Section 4: Obtaining user input](#section-4-obtaining-user-input)
  - [Ex 1: User input Tasks](#ex-1-user-input-tasks)
- [Task 1: User Input and Conditional Statements](#task-1-user-input-and-conditional-statements)
- [Task: Temperature Converter](#task-temperature-converter)
- [Extra task](#extra-task)


# Section 1: Comparisons and Conditionals

## Exercise 1

Comparison of two values

```python
is_true = True
is_true = 5 > 4
print(is_true)
```

Output when run

```console
True
```

## Exercise 2

Logical Operators

```python
age = 25
is_in_age_range = age > 20 and age < 30

print(is_in_age_range)
```

Output when run

```console
True
```

## Exercise 3

```python
age = 16
# converting age to an integer for calculations
age = int(age)
age_group = "child"

if age > 18:
    age_group = "adult"

print(f"The age group is {age_group}")
```

Output when run

```console
The age group is child
```

## Exercise 4

```python
# Ex 4: if - else Conditionals
wind_speed = 9

if wind_speed < 10:
    print("It is a calm day")
else:
    print("It is a windy day")
```

Output when run

```console
It is a calm day
```
## Exercise 5

```python
# Ex 5: if - elif - else Conditionals
grade = 88

if grade < 50:
    print("You failed")
elif grade < 60:
    print("You passed")
elif grade < 70:
    print("You got a good pass")
else:
    print("You got an excellent pass")
```

Output when run

```console
You got an excellent pass
```

## Exercise 6

```python
# Ex 6: Summary Tasks
temperature1 = 10
temperature2 = 10

if temperature1 == temperature2:
    print("temperture 1 and tenperature2 are equal")
else:
    print("The 2 temperatures are not equal")
```

Output when run

```console
temperture 1 and tenperature2 are equal
```

# Section 2 : Python Lists
## Ex 1: Creating a List 

```python
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
```
## Ex 2: Accessingn a List 

```python
#Ex 2: Accessing a list
second_item = string_list[1] # will store "banana" in the 2nd item
string_list[0:2] # will return ["apple", "banana"]
last_item = string_list[-1] #will store "grape in the last_item
```

## Ex 3: Modifying a List

```python
#Ex 3: Modifying a list
string_list[0] = "pear"
string_list.append("orange")
#Task: add the item "Manchester" to the end of the city_list list
city_list.append("Manchester")
print(city_list)

city_list[1] = "Birmingham"
print(city_list)
```

Output when run

```
['Glasgow', 'London', 'Edinburgh', 'Manchester']
['Glasgow', 'Birmingham', 'Edinburgh', 'Manchester']
```

## Ex 4: Summary Task
## Task: CREATE, ACCESS & MODIFY Lists

```python
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
```

Output when run

```console
['red', 'pink', 'orange']
pink
['gold', 'pink', 'orange']
3
red is not in the list
['pink', 'orange']
```

# Section 3: Python Loops
## Exercise 1: While Loops

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

Output when run

```console
0
1
2
3
4
```

## Exercise 2: For Loops

```python
for fruit in string_list:
    print(fruit)

#Task: Create a for loop that prints each item
#in the city_list list
for city in city_list:
    print(city)
```

Output when run

```console
pear
banana
 orange
grape
orange
Glasgow
Birmingham
Edinburgh
Manchester
```

## Exercise 3: Loop keywords: range, break and continue

```python
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

#to continue counting from 0 to 4, but skip the
#number 2, we can do this by using the continue
#keyword inside an if statement like this:
for i in range(5):
    if i == 2:
        continue
    print(i)
```

Output when run

```console
0
1
2
3
4
0
1
2

0
1
3
4
```

# Exercise 4: Summary Tasks
## Task: Even numbers

```python
#create a list of numbers from 1 to 10
#use a for loop to iterate through the list and  
#only print the even unumbers (Hint: use the
#modulo % operator)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number % 2 == 0:
        print(number)
```

Output when run

```console
2
4
6
8
10
```

```python
#Sum of Squares
sum_of_squares = 0
for i in range(6):
    sum_of_squares += i ** 2
    print(sum_of_squares)
```

Output when run

```console
0
1
5
14
30
55
```

```python
#Task: Countdown
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Liftoff!")
```

Output when run

```console
10
9
8
7
6
5
4
3
2
1
Liftoff!
```

# Section 4: Obtaining user input

```python
user_input = input("Enter something: ")
print("You entered: ", user_input)

age = input("How old are you? ")

#Convert the age to an integer
age = int(age)

next_year_age = age + 1
print("Next year, you'll be", next_year_age, "years old.")

```

Output when run

```console
You entered:  Hi
Next year, you'll be 8 years old.
```

## Ex 1: User input Tasks
# Task 1: User Input and Conditional Statements

```python
users_age = input("Enter your age: ")
users_age = int(users_age)
if users_age < 18:
    print("You are a minor.")
elif users_age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.") 
```

Output when run

```console
You are an adult 
```

# Task: Temperature Converter

```python
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
```

Output when run

```console
Welcome to temperature converter
Enter a temperature in Celsius: 16
The temperature you have entered is 16 Celsius.
16 Celsius is equivalent to 62 Fahrenheit
16 Celsius is equivalent to 289.15 Kelvin
```

# Extra task

```python
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
```

Output when run

```console
Welcome to Temperature Converter Extra
Enter a temperature in Celsius:10
Would you like to convert to F or K? Enter F or K:k
The temperature you have entered is 10 Celsius.
10 Celsius is equivalent to 289.15 Kelvin.

Welcome to Temperature Converter Extra
Enter a temperature in Celsius:12
Would you like to convert to F or K? Enter F or K:f
The temperature you have entered is 12 Celsius.
12 Celsius is equivalent to 289.15 Kelvin.
```


