a = 1
b = 2
c = a + b # The variable 'c' is now equal to 3 or 'a' + 'b'.
# Calculate 'c' to be 'a' + 'b', or 3. The value will stay stored in this variable.
print(c)

a = 2 # We will change the value of 'a' to 2. Variables can be changed in Python, otherwise known as mutable.
b = 2
c = a + c # This now becomes 3 + 2, because we have calculated 'c' to be 3.
# The value of 'c' is still 3 from earlier, now resulting in 5 because we've added 'a' or 2.
print(c)

a = 2
b = 2
c = a + c # The variable 'c' is now 5 from earlier.
# The value of 'c' is now 7, as we have added 'a' to 'c', or 2 + 5.
print(c)
