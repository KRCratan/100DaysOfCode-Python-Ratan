# Python
## Python is one of the most popular programming languages. It’s simple to use, packed with features and supported by a wide range of libraries and frameworks. Its clean syntax makes it beginner-friendly.

- A high-level language, used in data science, automation, AI, web development and more.
- Known for its readability, which means code is easier to write, understand and maintain.
- Backed by strong library support, we don’t have to build everything from scratch.

## Application of Python
1. Web Development
2. Data Science and Machine Learning
3. Automation and Scripting
4. Web Scraping
5. Game Development
6. Desktop Application

### Web development
Python is used to build the backend (server side) of websites and web apps, handling things like user accounts, databases, and page logic using frameworks such as Django or Flask. It lets developers quickly create, update, and scale interactive sites that users access through a browser.

### Data science and machine learning
Python is used to analyze data, find patterns, and build predictive models using libraries like NumPy, pandas, scikit‑learn, TensorFlow, and PyTorch. It helps data scientists clean data, visualize it, and train models for tasks like predictions, recommendations, and classification.

### Automation and scripting
Python is used to write small programs (scripts) that automatically perform repetitive tasks such as renaming files, sending emails, backing up data, or managing system tasks. This saves time and reduces human errors by letting the computer handle routine work.

### Web scraping
Python is used to collect data from websites by sending requests to web pages and extracting specific information, often with libraries like Beautiful Soup, Scrapy, or Selenium. This is useful for building datasets from public sites, tracking prices, gathering news, or monitoring changes on web pages.

### Game development
Python is used to create simple 2D games or to prototype game logic using libraries like Pygame or as a scripting language inside larger game engines. It helps developers handle things like player movement, scoring, levels, and basic graphics and sound.

### Desktop applications
Python is used to build standalone software that runs on a user’s computer with a graphical user interface (GUI), such as note‑taking apps, calculators, or small tools. Libraries like Tkinter, PyQt, or Kivy let developers create windows, buttons, menus, and other interactive elements.


## Basic Code 
```python
print(Hello World!)

```

## Comments
- Comments are used to add explanatory notes within the code. They are ignored by the compiler and are meant for human understanding.
In Python, there are two ways to write comments:
###  Single-line comments using the # symbol:

```python
# This is a comment
print("Hello!")  # This prints "Hello!"

# You can use comments to explain your code
print("Python is fun!")  # This will show on the screen
```
### Multi-line comments using triple quotes ("""):

```python 
"""
This is a multi-line comment.
You can write multiple lines
of explanation here.
"""
print("Welcome!")
```

# Variables

## Python variables are:
- Dynamically typed
- Case-sensitive
- Cannot start with numbers

### Python Built-in Data Types
Common data types:

Type | Example
|-----|--------|
int |	10
float | 3.14
str	| "Hello"
bool |	True / False
list |	[1, 2, 3]
tuple |	(1, 2, 3)
dict |	{"name": "Ratan", "age": 21}
set |	{1, 2, 3}

## Number
- Variables are containers that hold data values. They are used to store, manipulate, and display information within a program.

- In short, a variable is like a memory unit that we can access by typing the name of the variable. 

- Each variable has a unique name and a value that can be of different types. Python is capable of automatically detecting the variable type, which makes coding more efficient.

### To initialize a variable, we use the following format:
```python
variable_name = value
```
### Let's take a look at the different types of numbers:
- int - an integer, such as 1 or -2.
- float - real number, such as 1.32 or 0.98.

- To initialize a variable of type int with the name a and the value 3:
```python
a = 3
```
- To initialize a variable of type float with the name b and the value 13.2:
```
b = 13.2
```

## String
- A char is a single character (for example: 1, 6, %, b, p, ., T, etc.)
- The str (string) type is a special type that consists of multiple chars.

To initialize a string value in a variable, enclose it within single or double quotation marks:
```python
s1 = 'This is a string'
s2 = "This is also a string"
```

## Boolean 
- A bool (Boolean) type has only 2 possible values: True or False.

Here is an example of assigning a bool value to a variable:
```python 
variable_true = True
variable_false = False
```
###### Booleans are the building blocks for creating logic in the programs we write.

## Naming Conventions
- Naming conventions are a set of guidelines that developers follow to make their code more readable and maintainable. Different programming languages often have different naming conventions. In python, variables are written in snake case - words are separated by underscores

When writing a variable name be descriptive and use meaningful words
For example:
```python
# Bad Naming
isActive = False # not snake case
a = 10
b = "Hello"
x = True

# Good Naming
age = 10
greeting = "Hello"
is_active = True
```

##  Empty Variables
- In Python, None is a special value that represents "nothing" or "no value." It's like an empty box - it exists, but there's nothing inside it. For example:
```python
empty_box = None
```
- In a real scenario you could use None to indicate that something was not initialized yet.
For example:
```python
score = None  # Score hasn't been calculated yet
name = None   # Name hasn't been entered yet 
```

## Type Casting (Conversion)
- The process of explicitly converting a value from one data type to another (such as converting a string to an integer, integer to float, etc.) using built-in functions like int(), float(), str(), and list().

```python
x = "100"
num = int(x)     # converts string to integer

value = 3.99
text = str(value)  # converts float to string
```

## Taking User Input
- The process of collecting data from the user during program execution using the built-in input() function. The value received is returned as a string and can be further processed or converted to other data types as required.

- input() always returns a string.

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello", name, "you are", age, "years old")
```