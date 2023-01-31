import sys

if len(sys.argv) == 1:
    print("usage: python3 whois.py \"number\"")
    sys.exit(1)
else : 
    #check if the argument is a number and is just one argumeny
    if sys.argv[1].isdigit() and len(sys.argv) == 2:
        number = int(sys.argv[1])
        if number == 0:
            print("I'm Zero.")
        elif number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    else:
        print("ERROR In arguments")
