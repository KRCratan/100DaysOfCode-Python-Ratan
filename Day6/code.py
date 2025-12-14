# ================================
# Python Loops – Complete Examples
# ================================

# -------- For Loop (Basic) --------
n = 4
for i in range(0, n):
    print(i)

print("\n----------------\n")

# -------- Iterating Over List --------
li = ["geeks", "for", "geeks"]
for x in li:
    print(x)

print("\n----------------\n")

# -------- Iterating Over Tuple --------
tup = ("geeks", "for", "geeks")
for x in tup:
    print(x)

print("\n----------------\n")

# -------- Iterating Over String --------
s = "abc"
for x in s:
    print(x)

print("\n----------------\n")

# -------- Iterating Over Dictionary --------
d = {'x': 123, 'y': 354}
for x in d:
    print("%s  %d" % (x, d[x]))

print("\n----------------\n")

# -------- Iterating Over Set --------
set1 = {10, 30, 20}
for x in set1:
    print(x)

print("\n==============================\n")

# -------- Iterating Using Index --------
li = ["geeks", "for", "geeks"]
for index in range(len(li)):
    print(li[index])

print("\n==============================\n")

# -------- Looping Through a String --------
for x in "banana":
    print(x)

print("\n==============================\n")

# -------- break Statement (After Print) --------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

print("\n----------------\n")

# -------- break Statement (Before Print) --------
for x in fruits:
    if x == "banana":
        break
    print(x)

print("\n==============================\n")

# -------- continue Statement --------
for x in fruits:
    if x == "banana":
        continue
    print(x)

print("\n==============================\n")

# -------- range() Function --------
for x in range(6):
    print(x)

print("\n----------------\n")

# -------- range(start, end) --------
for x in range(2, 6):
    print(x)

print("\n----------------\n")

# -------- range(start, end, step) --------
for x in range(2, 30, 3):
    print(x)

print("\n==============================\n")

# -------- else in For Loop --------
for x in range(6):
    print(x)
else:
    print("Finally finished!")

print("\n----------------\n")

# -------- else with break --------
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")

print("\n==============================\n")

# -------- Nested Loops --------
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

print("\n==============================\n")

# -------- pass Statement --------
for x in [0, 1, 2]:
    pass

print("Pass loop executed without error")

print("\n==============================\n")

# -------- While Loop --------
cnt = 0
while cnt < 3:
    cnt = cnt + 1
    print("Hello Geek")

print("\n==============================\n")

# -------- Infinite While Loop (Commented for Safety) --------
# WARNING: Uncommenting this will cause an infinite loop
"""
while True:
    print("Hello Geek")
"""
