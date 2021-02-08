---
tutorial: "https://www.youtube.com/watch?v=fz4ttmwZWuc"
---

# `05` Defining vs Calling a function

Functions will only exists if you or somebody else defines them... it is the only way the language compiler/interpreter knows they exist, therefore it's able to run them when you call them.

To define a function we need to write this basic code formula:

```python
def myFunctionName(parameter, parameter2, ...parameterX):
    # the function code here
    return something
```

The word `def` is a reserved word in Python, this means it is only used to define a function.

**The name** of the function could be anything you like. 
Tip: use a descriptive name (don't be cheap with words, 
use as many as you need) this way you will understand what the function 
does -and returns-.
Example names: add_two_integers , calculate_taxes , get_random_number, etc.

**Parameters:** you can define as many parameters as you like or need. 
The amount of parameters will depend on the operations done inside the function, 
I.E: if the function is adding two integers  `(3 + 4)`  this means the function 
will need two parameters (one for each integer).

**Scope:** All the code that the function will contain need to be indented
 one tab to the right, anything on a different indentation 
won't be considered as part of the function, 
this is called **the scope**, and it could be local (inside the function) 
and global (outside of the function).

**The Return**: not every function needs to return something, but it is recommended that it does.
Tip: returning `None` is a good default for when you, still, don't know if you need to return something.

Example of a function:

```python
def concatenate_number_to_string(local_number, local_string):
    local_variable = local_string+""+str(local_number)
    return local_variable
```


# 📝 Instructions:

1. Define a function called "multi".
2. Multi function receive two numbers
3. Return the result of the multiplication between them.

# 💡 Hint

Remember to add the "return" line, every function must return something, in this case it should be the result of the multiplication.
