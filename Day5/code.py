# ==============================================
# Conditional Statements in Python
# ==============================================


# ----------------------------------------------
# 1. Simple if statement
# ----------------------------------------------
age = 20
if age >= 18:
    print("Eligible to vote.")

# Output:
# Eligible to vote.


# ----------------------------------------------
# 2. Short-hand if statement
# ----------------------------------------------
age = 19
if age > 18: print("Eligible to Vote.")

# Output:
# Eligible to Vote.


# ----------------------------------------------
# 3. If-else statement
# ----------------------------------------------
age = 10
if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")

# Output:
# Travel for free.


# ----------------------------------------------
# 4. Short-hand if-else (Ternary Operator)
# ----------------------------------------------
marks = 45
res = "Pass" if marks >= 40 else "Fail"
print(f"Result: {res}")

# Output:
# Result: Pass


# ----------------------------------------------
# 5. elif statement
# ----------------------------------------------
age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")

# Output:
# Young adult.


# ----------------------------------------------
# 6. Nested if-else statement
# ----------------------------------------------
age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")

# Output:
# 30% senior discount!


# ----------------------------------------------
# 7. Ternary conditional statement
# ----------------------------------------------
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)

# Output:
# Adult


# ----------------------------------------------
# 8. Match-case statement (Python 3.10+)
# ----------------------------------------------
number = 2

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")

# Output:
# Two or Three
