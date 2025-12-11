'''
Challenge:

Write code that checks if a person is eligible to drive. A person is eligible to drive if ALL of the following conditions are met:

The person is at least 18 years old
The person has a license
The person has insurance
Your program should:

Read an integer age from the first line of input
Read a string has_license from the second line of input (either "true" or "false")
Read a string has_insurance from the third line of input (either "true" or "false")
Convert the license and insurance inputs to boolean values
Check all three conditions and store the result in a variable named result
Print the final result (should be True or False)
'''

age = int(input("Enter Your age: "))
has_license = input().lower() == "true"
has_insurance = input().lower() == "true"
age = age >= 18
has_license = has_license == True
has_insurance = has_insurance == True
result =  age & has_license & (has_insurance)     # Complete this line to check if all conditions are met 

print(result)