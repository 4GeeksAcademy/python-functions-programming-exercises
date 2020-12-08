---
tutorial: "https://www.youtube.com/watch?v=HACQ9uerCuE"
---


# `06` Lambda functions in Python

A lambda function is a function with just one line of code and no name.
It is a very special type of funcion in the world of python because you can use it as a small utility for very agile coding:

```python
# declaring a normal funcion for multiplication
def multiply(p1, p2):
    return p1 * p2

# declaring it now like a one line lambda
multiply = lambda p1,p2: p1 * p2
```

1. Lambda fuctions have to be always very small
2. Lambda function can only have one line
3. Lambda don't need a `return` statement, it is assumed that it will return whatever is on that one line.
4. Lambda functions can be stored in variables or passed as parameters to another function

# 📝 Instructions:

1. Create a variable called `is_odd`
2. Assign a lambda function to it that returns True or False if a given number is odd

## 💡Hint

Here is how you would declare it like a normal function

```python
# this function return True if a number is odd.
def is_odd(num):
    return (num % 2) !== 0:
```
 
