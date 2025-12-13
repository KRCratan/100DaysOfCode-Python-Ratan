# Python Keywords  

Keywords in Python are special reserved words that are part of the language itself. They define the rules and structure of Python programs, which means you **cannot use them as names for variables, functions, classes, or other identifiers**.

---

## Getting List of All Python Keywords

We can get all Python keywords using the following code:

```python
import keyword
print("The list of keywords are : ")
print(keyword.kwlist)
```

### Output
```
The list of keywords are: 
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 
 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 
 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 
 'try', 'while', 'with', 'yield']
```

---

## Identify Python Keywords

### 1. With Syntax Highlighting  
Most IDEs provide syntax highlighting. Keywords appear in different colors or styles.

### 2. Using SyntaxError  
If you use a keyword incorrectly (e.g., as a variable name), Python raises a `SyntaxError`.

---

## Keywords as Variable Names

Example:

```python
for = 10
print(for)
```

### Output
```
  File "Solution.py", line 1
    for = 10 
        ^
SyntaxError: invalid syntax
```

Because `for` is a **reserved keyword**, it cannot be used as a variable name.

---

## Categorization of Python Keywords

| Category                | Keywords |
|------------------------|----------|
| **Value Keywords**     | True, False, None |
| **Operator Keywords**  | and, or, not, is, in |
| **Control Flow**       | if, else, elif, for, while, break, continue, pass, try, except, finally, raise, assert |
| **Function & Class**   | def, return, lambda, yield, class |
| **Context Management** | with, as |
| **Import & Module**    | import, from |
| **Scope & Namespace**  | global, nonlocal |
| **Async Programming**  | async, await |

---

## Keywords vs Identifiers

| Keywords | Identifiers |
|---------|-------------|
| Reserved words with predefined meanings. | Names for variables, functions, classes, etc. |
| Cannot be used as variable names. | Can be used if not a keyword. |
| Examples: `if`, `else`, `for`, `while`. | Examples: `x`, `number`, `sum`, `result`. |
| Part of Python syntax. | User-defined names. |
| Cannot be redefined. | Can be redefined by the programmer. |

---

## Variables vs Keywords

| Variables | Keywords |
|----------|----------|
| Used to store data. | Reserved words with predefined functions. |
| Can be created, modified, deleted. | Cannot be modified or reused as variable names. |
| Examples: `x`, `age`, `name`. | Examples: `if`, `while`, `for`. |
| Hold values manipulated in program. | Define structure and flow of code. |
| Flexible naming rules. | Fixed by Python; cannot be altered. |

---
