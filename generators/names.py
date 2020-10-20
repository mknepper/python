import random
name1 = ("Test1", "Test2", "Test3")
name2 = ("Test4", "Test5")
f = random.choice(name1)
s = random.choice(name2)
name = (f + " " + s)
print ("Name is: " + name)
