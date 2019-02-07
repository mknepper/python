# Useful Stuff

This contains commands, modules and other cool things you might want to know about Python 3. It's also something I use to cement things I learn. Enjoy.

### List All Functions in a Module

```python
# Where 'module' is the name of your desired module (ex. math):

import module
everything = dir(module)
print(everything)
```

### Convert Input to A String, Integer or Float


```Python
# For integers:

user_input=int(input())

# For floating point:

user_input=float(input())

# By default, user input is a string:

user_input=input()

# But if you really want to be sure, you can also do this:

user_input=str(input())```
