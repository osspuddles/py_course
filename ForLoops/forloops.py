#!/usr/bin/python3

# Simplest implementation (Remember we start with 0)
for i in range(1, 20):
    print("i is now {}".format(i))

# loop control variables are one of the only places where single-character variable names (specifically i & j) are
# acceptable.  The following example lists each digit of "number", one per line:
number = "4,167,098,381,123,671"  # set the variable
for i in range(0, len(number)):
    print(number[i])

# The following is the same, but excluding the commas.  This is achieved with an if statement that specifies which
# characters are acceptable
number = "4,167,098,381,123,671"  # set the variable
for i in range(0, len(number)):
    if number[i] in '0123456789':
        print(number[i])

# The values are displayed one per line because the print statement defaults to "end=\n".
# We can defeat this by specifying an empty string.
# The following prints out the number left-to-right as was originally entered, but removes the commas
number = "4,167,098,381,123,671"  # set the variable
for i in range(0, len(number)):
    if number[i] in '0123456789':
        print(number[i], end='')
# Using unqualified print statement will result in a newline after all iterations are complete.
# Otherwise, the next output will append to the last character of this output.
print("")

# To do math on the number, we need to convert it to an integer as well.  Here, we'll create an empty variable,
# cleanNumber, to hold the string until we are ready to convert.
number = "4,167,098,381,123,671"  # set the variable
cleanNumber = ''  # create empty variable
for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanNumber = cleanNumber + number[i]  # Appends one digit at a time to our string to be converted
newNumber = int(cleanNumber)  # The conversion from str to int
print("The number is {}".format(newNumber))
print("The square of the number is {}".format(newNumber ** 2))
