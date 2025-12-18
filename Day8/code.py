# =====================================
# Python Tuple Demonstration
# =====================================

print("----- Creating Tuples -----")

tup = ()
print(tup)

# Using String
tup = ('Geeks', 'For')
print(tup)

# Using List
li = [1, 2, 4, 5, 6]
print(tuple(li))

# Using Built-in Function
tup = tuple('Geeks')
print(tup)


print("\n----- Tuple with Mixed Datatypes -----")

tup = (5, 'Welcome', 7, 'Geeks')
print(tup)

# Nested tuples
tup1 = (0, 1, 2, 3)
tup2 = ('python', 'geek')
tup3 = (tup1, tup2)
print(tup3)

# Tuple repetition
tup1 = ('Geeks',) * 3
print(tup1)

# Tuple creation using loop
tup = ('Geeks')
n = 5
for i in range(int(n)):
    tup = (tup,)
    print(tup)


print("\n----- Tuple Accessing -----")

tup = tuple("Geeks")
print(tup[0])          # Indexing
print(tup[1:4])        # Slicing
print(tup[:3])

# Tuple unpacking
tup = ("Geeks", "For", "Geeks")
a, b, c = tup
print(a)
print(b)
print(c)


print("\n----- Tuple Concatenation -----")

tup1 = (0, 1, 2, 3)
tup2 = ('Geeks', 'For', 'Geeks')
tup3 = tup1 + tup2
print(tup3)


print("\n----- Tuple Slicing -----")

tup = tuple('GEEKSFORGEEKS')
print(tup[1:])     # Remove first element
print(tup[::-1])   # Reverse tuple
print(tup[4:9])    # Range slicing


print("\n----- Deleting a Tuple -----")

tup = (0, 1, 2, 3, 4)
del tup
try:
    print(tup)
except NameError as e:
    print(e)


print("\n----- Tuple Unpacking with Asterisk (*) -----")

tup = (1, 2, 3, 4, 5)
a, *b, c = tup
print(a)
print(b)
print(c)


# =====================================
# Python Set Demonstration
# =====================================

print("\n=============================")
print("----- Creating Sets -----")

set1 = {1, 2, 3, 4}
print(set1)

set1 = set()
print(set1)

set1 = set("GeeksForGeeks")
print(set1)

set1 = set(["Geeks", "For", "Geeks"])
print(set1)

tup = ("Geeks", "for", "Geeks")
print(set(tup))

d = {"Geeks": 1, "for": 2, "Geeks": 3}
print(set(d))


print("\n----- Unordered & Unindexed Set -----")

set1 = {3, 1, 4, 1, 5, 9, 2}
print(set1)

try:
    print(set1[0])
except TypeError as e:
    print(e)


print("\n----- Adding Elements to Set -----")

set1 = {1, 2, 3}
set1.add(4)
set1.update([5, 6])
print(set1)


print("\n----- Accessing Set Elements -----")

set1 = set(["Geeks", "For", "Geeks."])
for i in set1:
    print(i, end=" ")
print()

print("Geeks" in set1)


print("\n----- Removing Elements from Set -----")

set1 = {1, 2, 3, 4, 5}
set1.remove(3)
print(set1)

try:
    set1.remove(10)
except KeyError as e:
    print("Error:", e)

set1.discard(4)
print(set1)

set1.discard(10)
print(set1)


print("\n----- pop() Method -----")

set1 = {1, 2, 3, 4, 5}
val = set1.pop()
print(val)
print(set1)

set1.clear()
try:
    set1.pop()
except KeyError as e:
    print("Error:", e)


print("\n----- clear() Method -----")

set1 = {1, 2, 3, 4, 5}
set1.clear()
print(set1)


print("\n----- Frozen Set -----")

fset = frozenset([1, 2, 3, 4, 5])
print(fset)

set1 = {3, 1, 4, 1, 5}
fset = frozenset(set1)
print(fset)


print("\n----- Typecasting into Sets -----")

li = [1, 2, 3, 3, 4, 5, 5, 6, 2]
print(set(li))

s = "GeeksforGeeks"
print(set(s))

d = {1: "One", 2: "Two", 3: "Three"}
print(set(d))
