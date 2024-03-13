---
tutorial: "https://www.youtube.com/watch?v=vRusUCDa3-k"
---


# `05` Lambda Functions in Python

A **lambda function** is a function with just one line of code and no name.

It is a very special type of function in the world of Python because you can use it as a small utility for very agile coding:

```python
# Declaring a normal function for multiplication
def multiply(p1, p2):
    return p1 * p2

# Declaring it now like a one line lambda function
multiply = lambda p1,p2: p1 * p2
```

### 👉 Facts:

+ **Lambda functions** have to always be very small.

+ **Lambda functions** can only have one line.

+ **Lambda functions** don't need a `return` statement (it is assumed that it will return whatever is on that one line).

+ **Lambda functions** can be stored in variables or passed as parameters to another function.

## 📝 Instructions:

1. Create a variable called `is_odd`.

2. Assign a **lambda function** to it that returns `True` or `False` if a given number is odd.

## 💡 Hint

+ Here is how you would declare it like a normal function:

```py
# This function returns True if a number is odd
def is_odd(num):
    return num % 2 != 0
```

