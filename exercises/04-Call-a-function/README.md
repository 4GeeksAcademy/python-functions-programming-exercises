---
tutorial: "https://www.youtube.com/watch?v=NU5iW_bWwmY"
---

# `04` Calling a function  

A function could receive zero parameters, and it always returns something, even if you don't explicitly add the `return` statement.

:point_up: [Click here to read more about functions](https://content.breatheco.de/lesson/working-with-functions-python)

For example: a function that calculates the area of a square will be something like this:

```python
def calculate_area(length, edge):
    return length * edge
```

If you want to use that function to calculate the area of a square with:

```python
length = 3
edge = 6
```

You need to do something like this:
```python
area = calculate_area(3,6)
# The value of area will be set to 18
```

# 📝 Instructions:

Create a new variables named square_area1, square_area2, square_area3 and call the function calculate_area three times one for each square in the picture, for example: 

```python
# For the first figure:
square_area1 = calculate_area(4,4)
```

![img](http://i.imgur.com/VyoJRAL.png)

# 💡 Hint:

Call the `calculate_area` function three times, one per each square, passing the length and edge of each square.

:tv: [9 min video about functions in python](https://www.youtube.com/watch?v=NE97ylAnrz4)

