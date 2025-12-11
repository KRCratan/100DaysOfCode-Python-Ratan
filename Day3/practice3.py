"""
Challenge:

Complete the code to determine if a person is eligible to drive based on their age and license status.

A person is eligible to drive when:

They are at least 18 years old AND
They have a valid driving license
Fill in the blanks with the correct values:

Fill in the age variable with 20
Fill in the has_license variable with True
Fill in the minimum age requirement in the comparison
"""

age = 20
has_license = True

result = age >= 18 and has_license

# Don't change the line below
print("Eligible to drive:", result)