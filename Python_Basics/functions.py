# Python Functions

# Simple function

def greet():
    print("Hello, welcome to Python!")

greet()


# Function with parameters

def greet_user(name):
    print("Hello", name)

greet_user("Prajwal")


# Function with two parameters

def add(a, b):
    return a + b

result = add(10, 20)

print("Addition:", result)


# Function for checking even or odd

def check_even_odd(number):

    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print("10 is:", check_even_odd(10))
print("7 is:", check_even_odd(7))


# Function to calculate factorial

def factorial(number):

    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


print("Factorial of 5:", factorial(5))
