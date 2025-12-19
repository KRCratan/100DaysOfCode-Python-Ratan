# Dictionary
Python dictionary is a data structure that stores the value in key: value pairs. Values in a dictionary can be of any data type and can be duplicated, whereas keys can't be repeated and must be immutable.

- Keys are case sensitive which means same name but different cases of Key will be treated distinctly.
- Keys must be immutable which means keys can be strings, numbers or tuples but not lists.
- Duplicate keys are not allowed and any duplicate key will overwrite the previous value.
- Internally uses hashing. Hence, operations like search, insert, delete can be performed in Constant Time.
- From Python 3.7 Version onward, Python dictionary are Ordered.
  
## How to Create a Dictionary
Dictionary can be created by placing a sequence of elements within curly {} braces, separated by a 'comma'.
```python
d1 = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d1)

# create dictionary using dict() constructor
d2 = dict(a = "Geeks", b = "for", c = "Geeks")
print(d2)
```
Output
{1: 'Geeks', 2: 'For', 3: 'Geeks'}
{'a': 'Geeks', 'b': 'for', 'c': 'Geeks'}

## Accessing Dictionary Items
We can access a value from a dictionary by using the key within square brackets or get() method.
```python
d = { "name": "Prajjwal", 1: "Python", (1, 2): [1,2,4] }

# Access using key
print(d["name"])

# Access using get()
print(d.get("name"))
```
Output
Prajjwal
Prajjwal

## Adding and Updating Dictionary Items
We can add new key-value pairs or update existing keys by using assignment.
```python
d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
# Adding a new key-value pair
d["age"] = 22
# Updating an existing value
d[1] = "Python dict"
print(d)
```
Output
{1: 'Python dict', 2: 'For', 3: 'Geeks', 'age': 22}

## Removing Dictionary Items
We can remove items from dictionary using the following methods:
- del: Removes an item by key.
- pop(): Removes an item by key and returns its value.
- clear(): Empties the dictionary.
- popitem(): Removes and returns the last key-value pair.

```python
d = {1: 'Geeks', 2: 'For', 3: 'Geeks', 'age':22}

# Using del to remove an item
del d["age"]
print(d)

# Using pop() to remove an item and return the value
val = d.pop(1)
print(val)

# Using popitem to removes and returns
# the last key-value pair.
key, val = d.popitem()
print(f"Key: {key}, Value: {val}")

# Clear all items from the dictionary
d.clear()
print(d)
```
Output
{1: 'Geeks', 2: 'For', 3: 'Geeks'}
Geeks
Key: 3, Value: Geeks
{}

## Iterating Through a Dictionary
We can iterate over keys [using keys() method] , values [using values() method] or both [using item() method] with a for loop.
```python
d = {1: 'Geeks', 2: 'For', 'age':22}

# Iterate over keys
for key in d:
    print(key)

# Iterate over values
for value in d.values():
    print(value)

# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")
```
Output
1
2
age
Geeks
For
22
1: Geeks
2: For
age: 22


## Nested Dictionaries
![Nested Dictionary](image.png)

### Example of Nested Dictionary:
```python
d = {1: 'Geeks', 2: 'For',
        3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
​
print(d)
```
Output
{1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}



