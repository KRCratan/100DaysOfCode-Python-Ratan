# ===============================
# Python Lists – Complete Demo
# ===============================

# ---------- Creating Lists ----------

# Using Square Brackets
a = [1, 2, 3, 4, 5]                 # List of integers
b = ['apple', 'banana', 'cherry']   # List of strings
c = [1, 'hello', 3.14, True]        # Mixed data types

print("List a:", a)
print("List b:", b)
print("List c:", c)

print("-" * 40)

# Using list() Constructor
a = list((1, 2, 3, 'apple', 4.5))
print("List from tuple:", a)

b = list("GFG")
print("List from string:", b)

print("-" * 40)

# Creating List with Repeated Elements
a = [2] * 5
b = [0] * 7

print("Repeated list a:", a)
print("Repeated list b:", b)

print("-" * 40)

# ---------- Accessing List Elements ----------

a = [10, 20, 30, 40, 50]
print("First element:", a[0])
print("Last element:", a[-1])
print("Slice a[1:4]:", a[1:4])

print("-" * 40)

# ---------- Adding Elements to List ----------

a = []

a.append(10)
print("After append(10):", a)

a.insert(0, 5)
print("After insert(0, 5):", a)

a.extend([15, 20, 25])
print("After extend([15, 20, 25]):", a)

a.clear()
print("After clear():", a)

print("-" * 40)

# ---------- Updating Elements ----------

a = [10, 20, 30, 40, 50]
a[1] = 25
print("After updating index 1:", a)

print("-" * 40)

# ---------- Removing Elements ----------

a = [10, 20, 30, 40, 50]

a.remove(30)
print("After remove(30):", a)

popped_val = a.pop(1)
print("Popped element:", popped_val)
print("After pop(1):", a)

del a[0]
print("After del a[0]:", a)

print("-" * 40)

# ---------- Iterating Over a List ----------

a = ['apple', 'banana', 'cherry']
print("Iterating over list:")
for item in a:
    print(item)

print("-" * 40)

# ---------- Nested Lists ----------

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Element at matrix[1][2]:", matrix[1][2])

print("-" * 40)

# ---------- List Comprehension ----------

squares = [x ** 2 for x in range(1, 6)]
print("Squares using list comprehension:", squares)

print("-" * 40)

# ---------- How Python Stores List Elements ----------

a = [10, 20, "GfG", 40, True]

print("Complete list:", a)
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

print("-" * 40)

print("Program finished successfully.")
