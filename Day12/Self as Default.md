# Why Python Uses 'Self' as Default Argument
In Python, when defining methods inside a class, first parameter is always self. It is not a keyword, but a naming convention that plays a key role in Python’s object-oriented programming. The self parameter represents instance of the class itself, allowing you to access and modify its attributes and methods.
Code shows how self is used to store data in an object and access it through methods.
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Set instance attribute
        self.model = model  # Set instance attribute

    def display(self):
        return self.brand, self.model

# Create an instance of Car
car1 = Car("Toyota", "Corolla")

# Call the display method
print(car1.display())
```
Output
('Toyota', 'Corolla')

Explanation:

- self in __init__ assigns values (brand and model) to the specific instance (car1).
- self in display refers to the same instance (car1) to access attributes.
- Python automatically passes car1 as the first argument to display().

# Why use Self?
The main reason Python uses self is to make object-oriented programming explicit rather than implicit. By requiring the instance of the class as the first parameter, Python ensures:

- Clarity: Following Python’s “explicit is better than implicit” rule, it makes code easier to read.
- Flexibility: You can use any name (like this), but self is the standard.
- Consistency: Keeps all methods uniform across classes.
  
## Why Not Implicit?
Unlike some other programming languages, Python doesn’t hide this reference automatically. This makes it clear and unambiguous that the method is operating on an instance of the class, which improves readability and avoids confusion (especially in inheritance).

## Object Initialization & Method Invocation
In this example, self is used to initialize an object’s topic and access it inside a method.
```python
class gfg:
    def __init__(self, topic):
        self._topic = topic  # Store parameter value in instance variable

    def topic(self):
        print("Topic:", self._topic)  # Access the renamed variable

# Creating an instance of gfg
ins = gfg("Python")

# Calling the topic method
ins.topic()
```
Output
Topic: Python

Explanation:

- self._topic = topic assigns "Python" to the instance ins.
- Inside topic(), self._topic refers to that stored value (Python automatically provides self when you call ins.topic()).