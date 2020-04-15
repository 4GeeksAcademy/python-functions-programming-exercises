# `08` Functions that return


Is a very good practice that all functions return something, even if it is `None` if your functions return something you can then create algorithms that use several functions at the same time. For example, in this particular case we have two functions available:

```md
dollar_to_euro: that calculates the value in euros of a given value in dollars.
euro_to_yen: calculates the value in yen of a given value in euros.
```

# 📝 Instructions:
Using the two functions available, print on the console the value of 137 dollars in yen.

# 💡 Hint

Working backwards:
- Our expected value is in yen. 
- Our available function euro_to_yen will provide that
- To get to euro we will use the available function dollar_to_euro.