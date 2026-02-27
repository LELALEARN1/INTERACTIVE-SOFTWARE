def greet_user():
    print("Hello!")

greet_user()

def greet_user(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")

greet_user("John", "Smith")
greet_user(last_name="Smith", first_name="John")
            
def greet_user(first_name, last_name, university="UWS"):
    print(f"Hello {first_name} {last_name} from {university}!")
greet_user("John", "Smith")

greet_user("John", "Smith", "UWS London")
#or
greet_user("John", "Smith", university="UWS London")

#Task 1: Greeting message
friend_list = ["John", "Jane", "Jack"]
def greet_friends(names):
    for name in names:
        print("Hello", name, "!")

greet_friends(friend_list)

#Return
def add_numbers(num1, num2):
    return num1 + num1

def add_numbers(num1, num2):
    result = num1 + num2 #passing to a variable
    return result

result = add_numbers(5, 10)
print(result)

def add_and_multiply_numbers(num1, num2):
    return num1 + num2, num1 * num2

def add_and_multiply_numbers(num1, num2):
    sum = num1 + num2
    product = num1 * num2
    return sum, product

sum, product = add_and_multiply_numbers(5,10)
print(sum)
print(product)

#Task 2 Tax Calculation
def calculate_tax(income, tax_rate):
    tax = income * tax_rate
    print(tax)

calculate_tax(50000, 0.2)

#TASK: Compound Interest Calculator Function:
def with_interest(principal, duration, interest_rate):

    if interest_rate < 0 or interest_rate > 1:
        print("Please enter a decimal number between 0 and 1")

    if duration < 0:
        print("Please enter a positive number of years")

    for year in range(1, duration + 1):
        amount = principal * (1 + interest_rate) ** year
        amount = int(amount)
        print(f"Year {year}: {amount}")
        #return amount
        #principal = principal + amount
        #must return the calculated value
    
with_interest(1000, 5, 0.03)
print(with_interest)

#Exercise 2: Variable Scope

# def new_function():
#     my_new_variable = 5

# new_function() # call the function

#print(my_new_variable)
#generates an error because the variable has not been defined WITHIN the Function!

#So define the variable INSIDE the Function:
my_new_variable = 0

def new_function():
  my_new_variable = 10
  print(my_new_variable)

new_function()
#print(my_new_variable)

#Section 2: Assertions & Errors

#Ex3 : Assertions
#Python assertions are used to validate that certain conditions
#hold during program execution
#Assertions help ypur catch & handle errors early in your code
#Assertions generally are statements that check whether a given 
#condition is true
#If the condition is False, an AssertionError is raised,
#indicating a problem in the code
#Assertions are sueful for debugging & ensuring that your code
#works as expected & can stop problems from occurring before 
#they become severe

#If you built the function in Ex5 correctly, the following code
#should run without problems:

#assert compound_interest(1000, 5, 0.03)
assert with_interest(1000, 5, 0.03) == 1159
#????????

#Task1: Assertion
#Ex4: Identifying & Fixing Common Errors

#Section 3: Your first larger-scale Python programme
#Ex4: Complete template program

#Task: To-Do list manager
#in separate file in session 3 to_do_week_3.py

