# Arithmetic Operators
* Operators are used to perform operations on values.

|Operator | Operation | Example  |
|---------|-----------|--------- |
|   +     | Addition  | 3 + 2 = 5|
|   -     | Subtraction| 3 - 2 = 1 |
|   *     | Multiplication| 3 * 2 = 6|
|   /     | Division | 10 / 4 = 2.5|
|   //    | Floor Division | 10 // 4 = 2|
|   %     | Modulo (Remainder)     | 10 % 3 = 1 |
|   **    | Exponent  | 2 ** 3 = 8 |

Example:
```python

a = 10
b = 3

print(a + b)
print(a / b)
print(a // b)
print(a ** b)

```

### Modulo Operator
* The modulo operator % tells you what's left over after dividing one number by another.
```python
result = dividend % divisor
```
* dividend: The number being divided.
* divisor: The number that divides the dividend.
* result: The remainder of the division.

For Example:
```python
result = 10 % 3
```
Here, 10 is divided by 3. 3 goes into 10 three times, with a remainder of 1. So, result will be 1.
Usually modulo is used for checking if a number is even or odd:
* If a number is even, dividing it by 2 will leave a remainder of 0.
* If a number is odd, dividing it by 2 will leave a remainder of 1.

# Assignment Operators
Used to update variable values.
Python created a cool shortcut for self-arithmetic operations.

For example, instead of writing:
```python
a = 5
a = a + 3 # a holds 8
```
We can simplify it by writing += 
```python
a = 5
a += 3 # a holds 8
``` 
The += operator adds the value 3 to a.

| Operator | Meaning               | Equivalent             |
| -------- | --------------------- | ---------------------- |
| =        | Assign                | `x = 5`                |
| +=       | Add and assign        | `x += 3` → `x = x + 3` |
| -=       | Subtract and assign   | `x -= 2`               |
| *=       | Multiply and assign   | `x *= 4`               |
| /=       | Divide and assign     | `x /= 3`               |
| //=      | Floor divide & assign | `x //= 2`              |
| %=       | Modulo assign         | `x %= 2`               |
| **=      | Power assign          | `x **= 3`              |

# Comparison Operators
* Comparison operators are used to compare between two operands. 
* Output is boolean.

Sometimes we need to check whether an operand is greater than, less than, or equal to another operand. The following table shows possible operators for comparison:

| Operator | Meaning          | Example    |
| -------- | ---------------- | ---------- |
| ==       | Equal            | `5 == 5`   |
| !=       | Not equal        | `5 != 3`   |
| >        | Greater than     | `10 > 3`   |
| <        | Less than        | `2 < 5`    |
| >=       | Greater or equal | `10 >= 10` |
| <=       | Less or equal    | `3 <= 7`   |

Example:
```python
x = 10
y = 20

print(x == y)
print(x < y)
print(x >= 5)
```

# Logical Operators
* Used with boolean expressions.

| Operator | Meaning                      | Example             |
| -------- | ---------------------------- | ------------------- |
| and      | True only if both are True   | `x > 5 and x < 20`  |
| or       | True if at least one is True | `x > 20 or x == 10` |
| not      | Negates condition            | `not(x == 10)`      |


Example:
```python
age = 18
is_student = True

print(age >= 18 and is_student)
print(age < 18 or is_student)
print(not is_student)
```

* Logical operators have a special table called a **Truth Table** that shows what each combination of logical values returns.

## Truth Table for the `and` Operator

| a     | b     | a and b |
|-------|-------|----------|
| False | False | False    |
| False | True  | False    |
| True  | False | False    |
| True  | True  | True     |

**Condition for True:**  
Both `a` **and** `b` must be True.

---

## Truth Table for the `or` Operator

| a     | b     | a or b |
|-------|-------|---------|
| False | False | False   |
| False | True  | True    |
| True  | False | True    |
| True  | True  | True    |

**Condition for True:**  
Either `a` **or** `b` must be True (even one is enough).

---

## Truth Table for the `not` Operator

| a     | not a |
|-------|--------|
| False | True   |
| True  | False  |

**Meaning:**  
`not` reverses the value.  
If `a` is False → `not a` is True.  
If `a` is True → `not a` is False.
