import sys
print("In this script, we're going to print some text to a file.")
with open('io.txt', 'w') as f:
    f.write("You wrote...\n")
    f.write(input("Enter text here: "))
    f.close()
sys.exit()
