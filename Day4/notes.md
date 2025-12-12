# Strings
* A string is a sequence of characters enclosed in quotes. It can include letters, numbers, symbols or spaces. Since Python has no separate character type, even a single character is treated as a string with length one. Strings are widely used for text handling and manipulation.

## Creating a String
* Strings can be created using either single ('...') or double ("...") quotes. Both behave the same.

Example: Creating two equivalent strings one with single and other with double quotes.
```python
s1 = 'Hello!!!'  # single quote
s2 = "Hello!!!"  # double quote
print(s1)
print(s2)
```
## Multi-line Strings
- Use triple quotes ('''...''' ) or ( """...""") for strings that span multiple lines. Newlines are preserved.

Example: Define and print multi-line strings using both styles.

```python
s = """I am Learning
Python String on GeeksforGeeks"""
print(s)

s = '''I'm a 
Geek'''
print(s)
```
## Accessing characters in String
- Strings are indexed sequences. Positive indices start at 0 from the left; negative indices start at -1 from the right as represented in below image:
![alt text](image.png)

Example 1: Access specific characters through positive indexing.
```python
s = "GeeksforGeeks"
print(s[0])   # first character
print(s[4])   # 5th character
```
**Note: Accessing an index out of range will cause an IndexError. Only integers are allowed as indices and using a float or other types will result in a TypeError.** 

Example 2: Read characters from the end using negative indices.
```python
s = "GeeksforGeeks"
print(s[-10])   # 3rd character
print(s[-5])    # 5th character from end
```

## String Slicing
- Slicing is a way to extract a portion of a string by specifying the start and end indexes. The syntax for slicing is ***string[start:end]***, where **start** starting index and **end** is stopping index (excluded).


Example: In this example we are slicing through range and reversing a string.
```python
s = "GeeksforGeeks"
print(s[1:4])    # characters from index 1 to 3
print(s[:3])     # from start to index 2
print(s[3:])     # from index 3 to end
print(s[::-1])   # reverse string
```

Output
eek
Gee
ksforGeeks
skeeGrofskeeG


## String Iteration
Strings are iterable; you can loop through characters one by one.

Example: Here, it print each character on its own line.
```python
s = "Python"
for char in s:
    print(char)
```
Output
P
y
t
h
o
n

## String Immutability
- Strings are immutable, which means that they cannot be changed after they are created. If we need to manipulate strings then we can use methods like concatenation, slicing or formatting to create new strings based on original.

Example: In this example we are changing first character by building a new string.
```python
s = "geeksforGeeks"
s = "G" + s[1:]   # create new string
print(s)
```
Output
GeeksforGeeks

## Deleting a String
- In Python, it is not possible to delete individual characters from a string since strings are immutable. However, we can delete an entire string variable using the del keyword.

Example: Here, we are using del keyword to delete a string.
```python
s = "GfG"
del s
```

***Note: After deleting the string if we try to access s then it will result in a NameError because variable no longer exists.***

## Updating a String
- As strings are immutable, “updates” create new strings using slicing or methods such as replace().

Example: This code fix the first letter and replace a word.
```python
s = "hello geeks"
s1 = "H" + s[1:]                   # update first character
s2 = s.replace("geeks", "GeeksforGeeks")  # replace word
print(s1)
print(s2)
```
Output
Hello geeks
hello GeeksforGeeks

Explanation:
s1: slice from index 1 onward and prepend "H".
s2: replace("geeks", "GeeksforGeeks") returns a new string.

## Common String Methods
