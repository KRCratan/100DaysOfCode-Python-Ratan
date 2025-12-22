# Function
Functions are a block of statements that does a specific task. The idea is to put some commonly or repeatedly done task together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again.
![Function](image.png)

## Defining a Function
We can define a function in Python, using the `def` keyword. A function might take input in the form of parameters.

The syntax to declare a function is:
![function_syntax](image-1.png)

###### Here, we define a function using def that prints a welcome message when called.
```python
def fun():
    print("Welcome to GFG")
```
## Calling a Function
After creating a function in Python we can call it by using the name of the functions followed by parenthesis containing parameters of that particular function.
```python
def fun():
    print("Welcome to GFG")
    
fun() # Driver code to call a function
```
Output
Welcome to GFG

## Function Arguments
Arguments are the values passed inside the parenthesis of the function. A function can have any number of arguments separated by a comma.

**Syntax:**
```python
def function_name(parameters):
    """Docstring"""
    # body of the function
    return expression
```

We will create a simple function in Python to check whether the number passed as an argument to the function is even or odd.
```python
def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))
```
Output
Even
Odd

## Types of Function Arguments
Python supports various types of arguments that can be passed at the time of the function call. In Python, we have the following function argument types in Python, Let's explore them one by one.

### 1. Default Arguments
A default argument is a parameter that assumes a default value if a value is not provided in the function call for that argument.
```python
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)
myFun(10)
```

Output
x:  10
y:  50

### 2. Keyword Arguments
In keyword arguments, values are passed by explicitly specifying the parameter names, so the order doesn’t matter.
```python
def student(fname, lname):
    print(fname, lname)

student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks')
```
Output
Geeks Practice
Geeks Practice

### 3. Positional Arguments
In positional arguments, values are assigned to parameters based on their order in the function call.
```python
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("Suraj", 27)

print("\nCase-2:")
nameAge(27, "Suraj")
```
Output
Case-1:
Hi, I am Suraj
My age is  27

Case-2:
Hi, I am 27
My age is  Suraj

### 4. Arbitrary Arguments
In Python Arbitrary Keyword Arguments,` *args and **kwargs` can pass a variable number of arguments to a function using special symbols. There are two special symbols:
- *args in Python (Non-Keyword Arguments)
- **kwargs in Python (Keyword Arguments)
  
This code separately shows non-keyword (*args) and keyword (**kwargs) arguments in the same function.
```python
def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

# Function call with both types of arguments
myFun('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks')
```
Output
Non-Keyword Arguments (*args):
Hey
Welcome
Keyword Arguments (**kwargs):
first == Geeks
mid == for
last == Geeks
 
## Function within Functions
A function defined inside another function is called an inner function (or nested function). It can access variables from the enclosing function’s scope and is often used to keep logic protected and organized.
```python
def f1():
    s = 'I love GeeksforGeeks'
    def f2():
        print(s)
        
    f2()
f1()
```
Output
I love GeeksforGeeks

## Anonymous Functions
In Python, an anonymous function means that a function is without a name. As we already know the def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions.
```python
def cube(x): return x*x*x   # without lambda
cube_l = lambda x : x*x*x  # with lambda

print(cube(7))
print(cube_l(7))
```
Output
343
343

## Return Statement in Function
The return statement ends a function and sends a value back to the caller. It can return any data type, multiple values (packed into a tuple), or None if no value is given.

Syntax:
```python
return [expression]
```
***Parameters: return ends the function, [expression] is the optional value to return (defaults to None).***
```python
def square_value(num):
    """This function returns the square
    value of the entered number"""
    return num**2

print(square_value(2))
print(square_value(-4))
```
Output
4
16

## Pass by Reference and Pass by Value
In Python, variables are references to objects. When we pass them to a function, the behavior depends on whether the object is mutable (like lists, dictionaries) or immutable (like integers, strings, tuples).
- Mutable objects: Changes inside the function affect the original object.
- Immutable objects: The original value remains unchanged.
```python
# Function modifies the first element of list
def myFun(x):
    x[0] = 20

lst = [10, 11, 12, 13]
myFun(lst)
print(lst)   # list is modified

# Function tries to modify an integer
def myFun2(x):
    x = 20

a = 10
myFun2(a)
print(a)     # integer is not modified
```
Output
[20, 11, 12, 13]
10
***Note: Technically, Python uses "pass-by-object-reference". Mutable objects behave like pass by reference, while immutable objects behave like pass by value***

## Recursive Functions
A recursive function is a function that calls itself to solve a problem. It is commonly used in mathematical and divide-and-conquer problems. Always include a base case to avoid infinite recursion.
```python
def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1) 
      
print(factorial(4))
```
Output
24
Here we have created a recursive function to calculate the factorial of the number. It calls itself until a base case (n==0) is met.

## pass Statement
The pass statement in Python is a placeholder that does nothing when executed.

- It is used to keep code blocks valid where a statement is required but no logic is needed yet.
- Examples situations where pass is used are empty functions, classes, loops or conditional blocks.

### In Functions
The pass keyword in a function is used when we define a function but don't want to implement its logic immediately. It allows the function to be syntactically valid, even though it doesn’t perform any actions yet.
```python
def fun():
    pass

fun() # Call the function
```
Explanation: fun() is defined but contains pass statement, so it does nothing when called and program continues execution without any errors.

### In Conditional Statements
Sometimes, when using conditional statements we may not want to perform any action for a condition but still need the block to exist. The pass statement ensures the code remains valid without adding logic.
```python
x = 10

if x > 5:
    pass  # Placeholder for future logic
else:
    print("x is 5 or less")
```
Explanation:
- When x > 5, the pass statement runs, so nothing happens.
- If x <= 5, else block executes and prints the message.

### In Loops
In loops, pass can be used to skip writing any action during a specific iteration while still keeping the loop structure correct.
```python
for i in range(5):
    if i == 3:
        pass  # Do nothing when i is 3
    else:
        print(i)
```
Output
0
1
2
4

Explanation:
- For i == 3, the pass statement ensures nothing happens.
- For other values, the loop prints the number.

### In Classes
The pass statement allows defining empty classes or methods that act as placeholders until actual functionality is added later.
```python 
class EmptyClass:
    pass  # No methods or attributes yet

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        pass  # Placeholder for greet method

# Creating an instance of the class
p = Person("Emily", 30)
```

Explanation:
- EmptyClass is valid even without methods or attributes because of pass.
- greet() method exists but does nothing yet, letting us build the structure first.