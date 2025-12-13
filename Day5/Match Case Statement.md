# Python Match Case Statement
The `match case` statement offers a powerful mechanism for pattern matching in Python. It allows us to perform more expressive and readable conditional checks. Unlike traditional `if-elif-else` chains, which can become unwieldy with complex conditions, the `match-case` statement provides a more elegant and flexible solution.

---

## Basic Example

```python
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
```
Explanation
- The function check_number(x) uses a match-case statement to compare the value of x to constants 10 and 20.
- If x equals 10, it prints "It's 10".
- If x equals 20, it prints "It's 20".
- If neither condition is met, the wildcard _ matches any value and prints "It's neither 10 nor 20".

## Python Match Case Statement Syntax
The `match-case` syntax is based on structural pattern matching, which enables matching against data structures like sequences, mappings, and even classes. This provides more granularity and flexibility in handling various conditions.
```python
match subject:
    case pattern1:
        # Code block if pattern1 matches
    case pattern2:
        # Code block if pattern2 matches
    case _:
        # Default case (wildcard) if no other pattern matches
```
Key Components
- match subject: The value (or variable) to match against.
- case pattern: A pattern to match the subject.
- _ (Wildcard): A default catch-all pattern, similar to a default case in other languages.

## Match Case Statements with Constants
Matching constants is one of the simplest uses of the `match-case` statement.
```python
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
```
Explanation
- The function checks the value of person.
- It matches "A" and "B" explicitly.
- If no match is found, the wildcard _ prints "Hello, stranger!".

## Match Case Statement with OR Operator
Multiple patterns can be combined using the `| (OR) ` operator.
```python
def num_check(x):
    match x:
        case 10 | 20 | 30:
            print(f"Matched: {x}")
        case _:
            print("No match found")

num_check(10)
num_check(20)
num_check(25)
```
Output
Matched: 10
Matched: 20
No match found

Explanation
- The pattern` 10 | 20 | 30 ` matches any of these values.
- If `x` is none of these, the wildcard `_` executes.

## Match Case Statement with If Condition (Guards)
We can add an `if` condition after a case to refine matching logic.
```python
def num_check(x):
    match x:
        case 10 if x % 2 == 0:
            print("Matched 10 and it's even!")
        case 10:
            print("Matched 10, but it's not even.")
        case _:
            print("No match found")

num_check(10)
num_check(15)
```

Explanation
- The first case matches `10` only if it satisfies the condition `x % 2 == 0`.
- The second case acts as a fallback for `10` without the condition.
- The wildcard `_` handles all other values.

## Match Case Statement on Sequences
The `match-case` statement is very effective when working with sequences like lists or tuples
```python
def process(data):
    match data:
        case [x, y]:
            print(f"Two-element list: {x}, {y}")
        case [x, y, z]:
            print(f"Three-element list: {x}, {y}, {z}")
        case _:
            print("Unknown data format")

process([1, 2])
process([1, 2, 3])
process([1, 2, 3, 4])
```
Explanation
- `[x, y]` matches lists with exactly two elements.
- `[x, y, z]` matches lists with exactly three elements.
Any other structure falls into the wildcard case.

## Match Case Statement on Mappings (Dictionaries)
Match-case can also be used to match dictionary structures.
```python
def person(person):
    match person:
        case {"name": name, "age": age}:
            print(f"Name: {name}, Age: {age}")
        case {"name": name}:
            print(f"Name: {name}")
        case _:
            print("Unknown format")

person({"name": "Alice", "age": 25})
person({"name": "Bob"})
person({"city": "New York"})
```

Explanation
- The first case matches dictionaries containing both `"name"` and `"age"`.
- The second case matches dictionaries with only `"name"`.
- The wildcard `_` handles all other dictionary formats.

## Match Case Statement with Python Classes
One of the most powerful features of `match-case` is class pattern matching.
```python
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
```
Explanation
- `Circle(radius)` matches a `Circle` object and extracts its `radius`.
- `Rectangle(width, height)` matches a `Rectangle` object and extracts its attributes.
- The wildcard `_` handles any unknown object.
