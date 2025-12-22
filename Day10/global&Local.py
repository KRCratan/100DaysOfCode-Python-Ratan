# =========================================
# Global and Local Variables - Complete Demo
# =========================================

# -------- Local Variables --------

# Example 1: Accessing local variable inside function
def greet():
    msg = "Hello from inside the function!"
    print(msg)

greet()


# Example 2: Trying to access local variable outside function (will cause error)
def greet_error():
    msg = "Hello!"
    print("Inside function:", msg)

greet_error()

# Uncomment below line to see NameError
# print("Outside function:", msg)


# -------- Global Variables --------

# Creating a global variable
msg = "Python is awesome!"

def display():
    print("Inside function:", msg)

display()
print("Outside function:", msg)


# -------- Local shadows Global --------

def fun_shadow():
    s = "Me too."
    print(s)

s = "I love GeeksforGeeks"
fun_shadow()
print(s)


# -------- Modifying Global Variable --------

# Without global keyword (causes error)
def fun_error():
    # Uncomment to see error
    # s += " GFG"
    # print(s)
    pass

s = "I love GeeksforGeeks"
# fun_error()


# With global keyword (works correctly)
s = "Python is great!"

def fun_global():
    global s
    s += " GFG"
    print(s)
    s = "Look for GeeksforGeeks Python Section"
    print(s)

fun_global()
print(s)


# -------- Global vs Local with Same Name --------

a = 1  # Global variable

def f():
    print("f():", a)

def g():
    a = 2  # Local variable
    print("g():", a)

def h():
    global a
    a = 3
    print("h():", a)

print("global:", a)
f()
print("global:", a)
g()
print("global:", a)
h()
print("global:", a)
