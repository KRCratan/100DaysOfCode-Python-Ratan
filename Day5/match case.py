# Python Match Case Statement – All Examples Combined
# Requires Python 3.10+

# --------------------------------------------------
# 1. Basic match-case example
# --------------------------------------------------
def check_number(x):
    match x:
        case 10:
            print("It's 10")
        case 20:
            print("It's 20")
        case _:
            print("It's neither 10 nor 20")

check_number(10)
check_number(30)


# --------------------------------------------------
# 2. Match-case with constants (string matching)
# --------------------------------------------------
def greet(person):
    match person:
        case "A":
            print("Hello, A!")
        case "B":
            print("Hello, B!")
        case _:
            print("Hello, stranger!")

greet("A")
greet("B")
greet("C")


# --------------------------------------------------
# 3. Match-case with OR operator
# --------------------------------------------------
def num_check_or(x):
    match x:
        case 10 | 20 | 30:
            print(f"Matched: {x}")
        case _:
            print("No match found")

num_check_or(10)
num_check_or(20)
num_check_or(25)


# --------------------------------------------------
# 4. Match-case with if condition (guard)
# --------------------------------------------------
def num_check_guard(x):
    match x:
        case 10 if x % 2 == 0:
            print("Matched 10 and it's even!")
        case 10:
            print("Matched 10, but it's not even.")
        case _:
            print("No match found")

num_check_guard(10)
num_check_guard(15)


# --------------------------------------------------
# 5. Match-case with sequences (lists / tuples)
# --------------------------------------------------
def process_sequence(data):
    match data:
        case [x, y]:
            print(f"Two-element list: {x}, {y}")
        case [x, y, z]:
            print(f"Three-element list: {x}, {y}, {z}")
        case _:
            print("Unknown data format")

process_sequence([1, 2])
process_sequence([1, 2, 3])
process_sequence([1, 2, 3, 4])


# --------------------------------------------------
# 6. Match-case with mappings (dictionaries)
# --------------------------------------------------
def process_person(person):
    match person:
        case {"name": name, "age": age}:
            print(f"Name: {name}, Age: {age}")
        case {"name": name}:
            print(f"Name: {name}")
        case _:
            print("Unknown format")

process_person({"name": "Alice", "age": 25})
process_person({"name": "Bob"})
process_person({"city": "New York"})


# --------------------------------------------------
# 7. Match-case with classes
# --------------------------------------------------
class Shape:
    pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

def check_shape(shape):
    match shape:
        case Circle(radius):
            print(f"Circle radius {radius}.")
        case Rectangle(width, height):
            print(f"Rectangle width {width} and height {height}.")
        case _:
            print("This is an unknown shape.")

circle = Circle(10)
rectangle = Rectangle(4, 6)

check_shape(circle)
check_shape(rectangle)
