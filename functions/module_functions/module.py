def addition():
    print("\nAdd two numbers!\n")
    x = int(input("Enter number 1: "))
    y = int(input("\nEnter number 2: "))
    z = x + y
    print("\nYou entered "+ str(x) +" and " + str(y) + ". Your sum is " + str(z) + ".")

def division():
    print("\nDivide two numbers!\n")
    x = float(input("Enter number 1: "))
    y = float(input("\nEnter number 2: "))
    z = x / y
    print("\nYou entered "+ str(x) +" and " + str(y) + ". Your quotient is " + str(float(z)) + ".")

def printed():
  print("Hello! Let's do some math! Only numbers will work; if you enter a letter or symbol, the program will crash! :( So use numbers only! That includes decimals!")

def remainder():
    print("\nGet the remainder of two numbers!\n")
    x = int(input("Enter number 1: "))
    y = int(input("\nEnter number 2: "))
    z = x % y
    print("\nYou entered "+str(x)+" and "+str(y)+". Your remainder is "+str(z)+" .")
