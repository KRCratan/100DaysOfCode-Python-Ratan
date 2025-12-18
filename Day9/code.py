# ================================
# Python Dictionary Demonstration
# ================================

# --- Creating Dictionaries ---

d1 = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d1)

# create dictionary using dict() constructor
d2 = dict(a="Geeks", b="for", c="Geeks")
print(d2)


print("\n--- Accessing Dictionary Items ---")

d = {"name": "Prajjwal", 1: "Python", (1, 2): [1, 2, 4]}

# Access using key
print(d["name"])

# Access using get()
print(d.get("name"))


print("\n--- Adding and Updating Dictionary Items ---")

d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

# Adding a new key-value pair
d["age"] = 22

# Updating an existing value
d[1] = "Python dict"
print(d)


print("\n--- Removing Dictionary Items ---")

d = {1: 'Geeks', 2: 'For', 3: 'Geeks', 'age': 22}

# Using del to remove an item
del d["age"]
print(d)

# Using pop() to remove an item and return the value
val = d.pop(1)
print(val)

# Using popitem() to remove and return the last key-value pair
key, val = d.popitem()
print(f"Key: {key}, Value: {val}")

# Clear all items from the dictionary
d.clear()
print(d)


print("\n--- Iterating Through a Dictionary ---")

d = {1: 'Geeks', 2: 'For', 'age': 22}

# Iterate over keys
for key in d:
    print(key)

# Iterate over values
for value in d.values():
    print(value)

# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")


print("\n--- Nested Dictionary ---")

d = {
    1: 'Geeks',
    2: 'For',
    3: {
        'A': 'Welcome',
        'B': 'To',
        'C': 'Geeks'
    }
}

print(d)
