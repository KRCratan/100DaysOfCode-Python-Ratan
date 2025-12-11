"""
Challenge:

You are given a code with variables b1, b2, and b3 that have question marks instead of values. Replace each question mark with either True or False so that the final result b4 will be True.

Important: Only replace the question marks in b1, b2, and b3. Do not modify the line that calculates b4 or any other lines.
"""

b1 = True
b2 = True
b3 = False

# Don't change the lines below
b4 = b1 and b2 and (not b3)
print(f"b4 = {b4}")