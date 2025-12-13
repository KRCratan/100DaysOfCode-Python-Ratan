# ============================================
# PYTHON STRING 
# ============================================

# ------------------------------------------------
# 1. CREATING A STRING
# ------------------------------------------------
s1 = 'GfG'          # single quote
s2 = "GfG"          # double quote
print(s1)
print(s2)

# Output:
# GfG
# GfG


# ------------------------------------------------
# 2. MULTI-LINE STRINGS
# ------------------------------------------------
s = """I am Learning
Python String on GeeksforGeeks"""
print(s)

s = '''I'm a 
Geek'''
print(s)

# Output:
# I am Learning
# Python String on GeeksforGeeks
# I'm a 
# Geek


# ------------------------------------------------
# 3. ACCESSING CHARACTERS IN STRING
# ------------------------------------------------
s = "GeeksforGeeks"
print(s[0])      # first char
print(s[4])      # 5th char

# Output:
# G
# s

print(s[-10])    # 3rd char from left
print(s[-5])     # 5th from end

# Output:
# k
# G


# ------------------------------------------------
# 4. STRING SLICING
# ------------------------------------------------
s = "GeeksforGeeks"
print(s[1:4])     # index 1→3
print(s[:3])      # beginning → index 2
print(s[3:])      # index 3 → end
print(s[::-1])    # reverse

# Output:
# eek
# Gee
# ksforGeeks
# skeeGrofskeeG


# ------------------------------------------------
# 5. STRING ITERATION
# ------------------------------------------------
s = "Python"
for char in s:
    print(char)

# Output:
# P
# y
# t
# h
# o
# n


# ------------------------------------------------
# 6. STRING IMMUTABILITY
# ------------------------------------------------
s = "geeksforGeeks"
s = "G" + s[1:]      # create new string
print(s)

# Output:
# GeeksforGeeks


# ------------------------------------------------
# 7. DELETING A STRING
# ------------------------------------------------
s = "GfG"
del s
# Trying to print s now would cause NameError


# ------------------------------------------------
# 8. UPDATING A STRING
# ------------------------------------------------
s = "hello geeks"
s1 = "H" + s[1:]                         # update first char
s2 = s.replace("geeks", "GeeksforGeeks")  # replace word
print(s1)
print(s2)

# Output:
# Hello geeks
# hello GeeksforGeeks


# ------------------------------------------------
# 9. COMMON STRING METHODS
# ------------------------------------------------

# len()
s = "GeeksforGeeks"
print(len(s))

# Output:
# 13

# upper() and lower()
s = "Hello World"
print(s.upper())
print(s.lower())

# Output:
# HELLO WORLD
# hello world

# strip() and replace()
s = "   Gfg   "
print(s.strip())

s = "Python is fun"
print(s.replace("fun", "awesome"))

# Output:
# Gfg
# Python is awesome


# ------------------------------------------------
# 10. CONCATENATING AND REPEATING STRINGS
# ------------------------------------------------

# Concatenation
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)

# Output:
# Hello World

# Repetition
s = "Hello "
print(s * 3)

# Output:
# Hello Hello Hello 


# ------------------------------------------------
# 11. FORMATTING STRINGS
# ------------------------------------------------

# f-strings
name = "Alice"
age = 22
print(f"Name: {name}, Age: {age}")

# Output:
# Name: Alice, Age: 22

# format()
s = "My name is {} and I am {} years old.".format("Alice", 22)
print(s)

# Output:
# My name is Alice and I am 22 years old.


# ------------------------------------------------
# 12. STRING MEMBERSHIP TESTING
# ------------------------------------------------
s = "GeeksforGeeks"
print("Geeks" in s)
print("GfG" in s)

# Output:
# True
# False
