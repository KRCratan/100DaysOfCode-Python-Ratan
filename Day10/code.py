# ================================
# Python Functions - Complete Demo
# ================================

# 1. Defining and Calling a Function
def fun():
    print("Welcome to GFG")

fun()


# 2. Function with Arguments (Even or Odd)
def evenOdd(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))


# 3. Default Arguments
def myFun(x, y=50):
    print("x:", x)
    print("y:", y)

myFun(10)


# 4. Keyword Arguments
def student(fname, lname):
    print(fname, lname)

student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks')


# 5. Positional Arguments
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is", age)

print("Case-1:")
nameAge("Suraj", 27)

print("\nCase-2:")
nameAge(27, "Suraj")


# 6. Arbitrary Arguments (*args and **kwargs)
def myFunArgs(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

myFunArgs('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks')


# 7. Function within Function (Nested Function)
def f1():
    s = 'I love GeeksforGeeks'
    def f2():
        print(s)
    f2()

f1()


# 8. Anonymous Function (Lambda)
def cube(x):
    return x * x * x

cube_l = lambda x: x * x * x

print(cube(7))
print(cube_l(7))


# 9. Return Statement Example
def square_value(num):
    """Returns square of a number"""
    return num ** 2

print(square_value(2))
print(square_value(-4))


# 10. Pass by Reference vs Pass by Value
def modify_list(x):
    x[0] = 20

lst = [10, 11, 12, 13]
modify_list(lst)
print(lst)

def modify_number(x):
    x = 20

a = 10
modify_number(a)
print(a)


# 11. Recursive Function (Factorial)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4))
