# Section 1: FUNCTIONS AND SCOPE

## Exercise 1
## Functions in Python

Creating Functions

```python
def greet_user():
    print("Hello!")

greet_user()

def greet_user(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")

greet_user("John", "Smith")
greet_user(last_name="Smith", first_name="John")
```

Output when run

```console
Hello!
Hello John Smith!
Hello John Smith!
```


```python
def greet_user(first_name, last_name, university="UWS"):
    print(f"Hello {first_name} {last_name} from {university}!")
greet_user("John", "Smith")

greet_user("John", "Smith", "UWS London")
#or
#Keyword arguments
greet_user("John", "Smith", university="UWS London")
```

Output when run

```console
Hello John Smith from UWS!
Hello John Smith from UWS London!
Hello John Smith from UWS London!
```

## Task 1: Greeting Message

```python
#Task 1: Greeting message
friend_list = ["John", "Jane", "Jack"]
def greet_friends(names):
    for name in names:
        print("Hello", name, "!")

greet_friends(friend_list)
```

Output when run

```console
Hello John !
Hello Jane !
Hello Jack !
```

## Return 

```python
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
```

Output when  run

```console
15
15
50
```

## Task 2: Tax Calculation

```python
#Task 2 Tax Calculation
def calculate_tax(income, tax_rate):
    tax = income * tax_rate
    print(tax)

calculate_tax(50000, 0.2)
```

Output when run

```console
10000.0
```

# Compound Tax Calculation

```python
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
```

Output when run

```console
Year 1: 1030
Year 2: 1060
Year 3: 1092
Year 4: 1125
Year 5: 1159
<function with_interest at 0x0000021D762E9C70>
```

