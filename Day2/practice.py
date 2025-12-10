'''
Objective:

Create a Python script that:
Asks the user for their name and age.
Greets them with a personalized message.
Tells them how old they will be next year.
'''
# Greeting Program

# Step 1: Take input from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Step 2: Create a greeting message
greeting = f"Hello {name}, nice to meet you!"

# Step 3: Calculate age for next year
next_year_age = age + 1

# Step 4: Display output
print(greeting)
print(f"You are {age} years old.")
print(f"Next year, you will be {next_year_age} years old!")
