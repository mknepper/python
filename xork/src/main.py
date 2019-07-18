## Written exclusively for Python 3. Enjoy!
## Importing some basic modules; sys for sys.exit, time for time.sleep() and string for .lower()
import sys
import time
import string
## Makes console wait one second before proceeding
time.sleep(1)
print("")
print("So begins your journey into darkness...")
print("")
print("If you wish to quit, enter Q into the console at anytime. Otherwise, let your journey begin...")
time.sleep(1)
## While loops; they run forever until condition is met (if you select '2', the loops terminates)
while True:
## I chose 'try' because it allows for error handling; using 'except', you can have it spit errors
## These errors can be generalized, how I have it, or for ints, strs, etc.
## I set it to 'pass' because we're not doing any error handling, because of the nature of the script
## If the 'try' is removed, the 'except' function is no longer needed
## If you keep try, you MUST use the 'except' function, with some specificity
    try:
        print("\nYour room is DARK, yet a light flashes red. What do you do?")
        print("")
        print("1. Look around.")
        print("2. There's a lamp somewhere...")
        print("3. Go back to bed.")
        print("")
        ans = (input(">>> ").lower())
        if ans == "1":
            print("")
            print("Too dark to see... better find a light...")
            time.sleep(2)
        elif ans == "2":
            print("")
            print("Fumbling, you turn on your nightstand lamp...")
            break
        elif ans == "3":
            print("")
            print("You sleep away the troubles... but you can't stay asleep...")
            time.sleep(1)
            print("")
            print("Back to the world of the living...")
        elif ans == "q":
            sys.exit(0)
        else:
            print("\nWhat?")
    except Exception:
        pass
print("")
time.sleep(1)
print("You see an unkempt room. Shame...")
print("")
time.sleep(1)
while True:
    try:
        print("What do you do?")
        print("")
        print("1. Explore.")
        print("2. Turn off lamp and go back to bed.")
        print("")
        ans = (input(">>> ").lower())
        if ans == "1":
            print("")
            print("You see a lot of stuff, including your DESK, a DOOR, and a DRESSER.")
            break
        elif ans == "2":
            time.sleep(1)
            print("")
            print("No matter how you try, you can't fall back asleep...")
            print("")
            time.sleep(1)
        elif ans == "q":
            sys.exit(0)
        else:
            print("\n...What?")
    except Exception:
        pass
time.sleep(1)
print("")
print("Now that you have a mental map of the room, what do you do?")
print("")
time.sleep(1)
while True:
    try:
        print("1. Check the DESK.")
        print("2. Check the DRESSER.")
        print("3. Check the DOOR.")
        print("4. Ignore everything...")
        print("5. Nothing left to check...")
        print("")
        ## This converts the input to all lower case, so we don't have to repeatedly specificy letter case
        ans = (input(">>> ").lower())
        if ans == "1":
            time.sleep(1)
            print("")
            print("You see a PICTURE, an issue of OVERCHROME, a KEYCARD and an ASHTRAY.")
            print("")
        elif ans == "2":
            time.sleep(1)
            print("")
            print("A pack of SMOKES, a LIGHTER and a HANDGUN with 2 BULLETS left in the clip.")
            print("")
        elif ans == "3":
            time.sleep(1)
            print("")
            print("Doesn't seem to want to open... must be locked...")
            print("")
        elif ans == "4":
            time.sleep(1)
            print("")
            print("Maybe after a couple seconds, you'll try things again...")
            print("")
        elif ans == "5":
            time.sleep(1)
            print("")
            print("Moving on...")
            break
        elif ans == "q":
            sys.exit(0)
        else:
            print ("\nI don't understand...")
    except Exception:
        pass
time.sleep(1)
print("")
print("It seems you have some items in your room, a locked door and other trinkets. What do you do?")
print("")
time.sleep(1)
while True:
    try:
        print("1. Read OVERCHROME magazine.")
        print("2. Light a cigarette, smoke it.")
        print("3. Grab the handgun, load it.")
        print("4. Use KEYCARD on door.")
        print("5. Something else...")
        print("")
        ans = (input(">>> ").lower())
        if ans == "1":
            time.sleep(1)
            print("")
            print("Something about breasts, guns and explosions. Is this important?")
            print("")
        if ans == "2":
           time.sleep(1)
           print("")
           print("Relaxing, but not good for your health. Maybe you should quit smoking at some point...")
           print("")
        if ans == "3":
           time.sleep(1)
           print("")
           print("You're cautious, so you load your pistol and ready it for use against any kind of enemy.")
           print("")
        if ans == "4":
           time.sleep(1)
           print("")
           print("The door opens... revealing flashing lights... and an open corridor...")
           print("")
           break
        if ans == "5":
           time.sleep(1)
           print("")
           print("No matter how hard you try, the temptation of opening the door nags...")
           print("")
        elif ans == "q":
           sys.exit(0)
        else:
           print("\nWhat??")
    except Exception:
        pass
## Kills the Python script - script complete!
sys.exit(0)
