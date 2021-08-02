
#---------------------------------------------------------
def foo(x):
    print("Hi, foo has been called with " + str(x))

print("We call foo before decoration:")
foo("Hi")
print('\n\n')
#---------------------------------------------------------

def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper

print('\n Custom Decorator..........')

print("\n We now decorate foo with f:")
foo = our_decorator(foo)
print("\n We call foo after decoration:")
foo(42)
print('\n\n')

#---------------------------------------------------------
# With Python Decorator
# The decoration occurs in the line before the function header.
# The "@" is followed by the decorator function name.

def our_new_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper

@our_new_decorator
def foo(x):
    print("Hi, foo has been called with " + str(x))

print('\n Python Decorator..........')

foo("Hi")
print('\n\n')

#--------------------------------------------------------

# A custom function
def display(str):
    print(str)

# Defining Custom Decorator Function with inner function
def display_decorator(fn):
    def display_wrapper(str):
        print('Output:  ')
        fn(str)
        print('Completed executing the function....')
    return display_wrapper

# Call the function
out = display_decorator(display)
out('Hello World')
print('\n\n')

#--------------------------------------------------------

@display_decorator
def display(str):
    print(str)

display('Hello India')

#--------------------------------------------------------

# The following program uses a decorator function to ensure that the argument
# passed to the function div is eith an integer or float and the denominator is not zero:

def denominator_test(func):
    def wrapper(x, y):
        if (type(y) == int or type(y) == float) and y == 0:
            raise Exception("Division by zero")
        
        if (type(x) == int or type(x) == float) and(type(y) == int or type(y) == float) and y!= 0:
            return func(x, y)
        else:
            if (type(x) != int or type(x) != float) and (type(y) != int or type(y) != float):
                 raise Exception("Data type mismatch")
            
    return wrapper
    
@denominator_test
def div(a, b):
    return a/b

print('\n Division..........')

for x, y in zip(range(10,16), range(2,8)):
	print(div(x,y))

#print(div('hello',2)) # Error - Data type mismatch
#print(div(3,0)) # Error - Division by zero

print('\n\n')
#--------------------------------------------------------

# The following program uses a decorator function to ensure that the argument
# passed to the function factorial is a positive integer:

def argument_test_natural_number(f):
    def helper(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            raise Exception("Argument is not an integer")
    return helper
    
@argument_test_natural_number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print('\n Factorial..........')
for i in range(1,10):
	print(i, factorial(i))

#print(factorial(-1)) # Error
print('\n\n')

#-----------------------------------------
# Static method
class Person:
    @staticmethod
    def greet():
        print("Hello!")

# Call with the name of the class
Person.greet()

# Call with an object
p1 = Person()
p1.greet()

print('\n\n')

#-----------------------------------------
# Class Method Decorator
# Person
class Employee:

    num_emp =0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Employee.num_emp +=1

    @classmethod
    def get_num_instance(cls):
        return Employee.num_emp

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

# Create two objects
e1 = Employee('Adam', 35)
e1.display()
e2 = Employee('Alice', 27)
e2.display()

# Check the number of instances with the name of the class
print(Employee.get_num_instance())

# Also callble from an object
print(e2.get_num_instance())


