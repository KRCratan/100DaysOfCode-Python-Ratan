# Set
Python set is an unordered collection of multiple items having different datatypes. In Python, sets are mutable, unindexed and do not contain duplicates. The order of elements in a set is not preserved and can change.

- Can store None values.
- Implemented using hash tables internally.
- Do not implement interfaces like Serializable or Cloneable.
- Python sets are not inherently thread-safe; synchronization is needed if used across threads.
  
## Creating a Set in Python
In Python, the most basic and efficient method for creating a set is using curly braces.
```python
set1 = {1, 2, 3, 4}
print(set1)
```
Output
{1, 2, 3, 4}

### Using the set() function
Python Sets can be created by using the built-in set() function with an iterable object or a sequence by placing the sequence inside curly braces, separated by a 'comma'.

***Note: A Python set cannot contain mutable types such as lists or dictionaries, because they are unhashable.***

```python
set1 = set()
print(set1)

set1 = set("GeeksForGeeks")
print(set1)

# Creating a Set with the use of a List
set1 = set(["Geeks", "For", "Geeks"])
print(set1)

# Creating a Set with the use of a tuple
tup = ("Geeks", "for", "Geeks")
print(set(tup))

# Creating a Set with the use of a dictionary
d = {"Geeks": 1, "for": 2, "Geeks": 3}
print(set(d))
```
Output
set()
{'e', 'r', 'o', 'k', 'G', 's', 'F'}
{'For', 'Geeks'}
{'for', 'Geeks'}
{'for', 'Geeks'}


### Unordered, Unindexed and Mutability
In set, the order of elements is not guaranteed to be the same as the order in which they were added. The output could vary each time we run the program. Also the duplicate items entered are removed by itself.

***Sets do not support indexing. Trying to access an element by index (set[0]) raises a TypeError.***

We can add elements to the set using add(). We can remove elements from the set using remove(). The set changes after these operations, demonstrating its mutability. However, we cannot changes its items directly.
```python
set1 = {3, 1, 4, 1, 5, 9, 2}

print(set1)  # Output may vary: {1, 2, 3, 4, 5, 9}

# Unindexed: Accessing elements by index is not possible
# This will raise a TypeError
try:
    print(set1[0])
except TypeError as e:
    print(e)
```
Output
{1, 2, 3, 4, 5, 9}
'set' object is not subscriptable

## Adding Elements to a Set in Python
We can add items to a set using add() method and update() method. add() method can be used to add only a single item. To add multiple items we use update() method.
```python
# Creating a set
set1 = {1, 2, 3}

# Add one item
set1.add(4)

# Add multiple items
set1.update([5, 6])

print(set1)
```
Output
{1, 2, 3, 4, 5, 6}

## Accessing a Set in Python
We can loop through a set to access set items as set is unindexed and do not support accessing elements by indexing. Also we can use in keyword which is membership operator to check if an item exists in a set.
```python
set1 = set(["Geeks", "For", "Geeks."])

# Accessing element using For loop
for i in set1:
    print(i, end=" ")

# Checking the element# using in keyword
print("Geeks" in set1)
```
Output
Geeks For Geeks. True

Explanation:
- This loop will print each item in the set. Since sets are unordered, the order of items printed is not guaranteed.
- This code checks if the number 4 is in set1 and prints a corresponding message.

## Removing Elements from the Set in Python
We can remove an element from a set in Python using several methods: remove(), discard() and pop(). Each method works slightly differently :
- Using remove() Method or discard() Method
- Using pop() Method
- Using clear() Method

### Using remove() Method or discard() Method
remove() method removes a specified element from the set. If the element is not present in the set, it raises a KeyError. discard() method also removes a specified element from the set. Unlike remove(), if the element is not found, it does not raise an error.
```python
# Using Remove Method
set1 = {1, 2, 3, 4, 5}
set1.remove(3)
print(set1)  

# Attempting to remove an element that does not exist
try:
    set1.remove(10)
except KeyError as e:
    print("Error:", e)  

# Using discard() Method
set1.discard(4)
print(set1)  

# Attempting to discard an element that does not exist
set1.discard(10)  # No error raised
print(set1)
```
Output
{1, 2, 4, 5}
Error: 10
{1, 2, 5}
{1, 2, 5}

***Note: If the set is unordered then there's no such way to determine which element is popped by using the pop() function. ***

## Using pop() Method
pop() method removes and returns an arbitrary element from the set. This means we don't know which element will be removed. If the set is empty, it raises a KeyError.
```python
set1 = {1, 2, 3, 4, 5}
val = set1.pop()
print(val)
print(set1)

# Using pop on an empty set
set1.clear()  # Clear the set to make it empty
try:
    set1.pop()
except KeyError as e:
    print("Error:", e)
```
Output
1
{2, 3, 4, 5}
Error: 'pop from an empty set'

## Using clear() Method
- clear() method removes all elements from the set, leaving it empty.
```python
set1 = {1, 2, 3, 4, 5}
set1.clear()
print(set1)
```
Output
set()

## Frozen Sets in Python
A frozenset in Python is a built-in data type that is similar to a set but with one key difference that is immutability. This means that once a frozenset is created, we cannot modify its elements that is we cannot add, remove or change any items in it. Like regular sets, a frozenset cannot contain duplicate elements.

If no parameters are passed, it returns an empty frozenset.  
```python
# Creating a frozenset from a list
fset = frozenset([1, 2, 3, 4, 5])
print(fset)  

# Creating a frozenset from a set
set1 = {3, 1, 4, 1, 5}
fset = frozenset(set1)
print(fset)
```
Output
frozenset({1, 2, 3, 4, 5})
frozenset({1, 3, 4, 5})

## Typecasting Objects into Sets
Typecasting objects into sets in Python refers to converting various data types into a set. Python provides the set() constructor to perform this typecasting, allowing us to convert lists, tuples and strings into sets.
```python
# Typecasting list into set
li = [1, 2, 3, 3, 4, 5, 5, 6, 2]
set1 = set(li)
print(set1)

# Typecasting string into set
s = "GeeksforGeeks"
set1 = set(s)
print(set1)

# Typecasting dictionary into set
d = {1: "One", 2: "Two", 3: "Three"}
set1 = set(d)
print(set1)
```

Output
{1, 2, 3, 4, 5, 6}
{'f', 'G', 's', 'k', 'r', 'e', 'o'}
{1, 2, 3}

