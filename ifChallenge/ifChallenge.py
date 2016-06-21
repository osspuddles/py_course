#!/usr/bin/python3

# Challenge: Write a small program to ask for a name and an age.
# When both values have been entered, check if the person is the right age to go on an 18-30 holiday.
# If they are, welcome them to the holiday, otherwise print a message refusing them entry.

name = input("Welcome!  Please enter your name: ")
if not name:
    print("You must enter a valid name!")
else:
    age = int(input("Please enter your age: "))
    if not age:
        print("You must enter your age")
    else:
        if 18 <= age <= 30:
            print("Welcome, %s, we've been expecting you!"
                  % name)  # String formatting operators (Python 2.x)
        elif age < 18:
            print("I'm sorry, {}, you are not old enough to board.  Please come back in {} years."
                  .format(name, 18 - age))  # Using replacement fields here (Python 3.x ONLY)
        else:
            print("I'm sorry, %s; maybe if it were %d years ago, we would let you on, but you're too old now."
                  % (name, age - 30))  # More than one field using SFO
