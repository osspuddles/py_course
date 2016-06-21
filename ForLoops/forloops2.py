#!/usr/bin/python3

number = "9,223,109,567,000,132"
cleanNumberString = ''

for char in number:  # Replacement for using len to determine number of iterations
    if char in '0123456789':
        cleanNumberString = cleanNumberString + char

newnumber = int(cleanNumberString)
print("The number is {}".format(newnumber))

for state in ["not pinin", "no more", "a stiff", "bereft of life", "an ex-parrot!"]:
    print("This parrot is {}".format(state))

# moving in steps.  a third number in the range determines step range
for i in range(0, 100, 5):
    print("i is {}".format(i))
print("\n")

# illustrating that these are steps, not multiples, by starting with 1 instead of 0:
for i in range(1, 100, 5):
    print("i is {}".format(i))

# Multiplication tables
for i in range(1, 13):
    for j in range(1, 13):
        print("{1} times {0} is {2}".format(j, i, j * i))
    print("=========================")
# same thing with string formatting operators (2.x)
for i in range(1, 13):
    for j in range(1, 13):
        print("%d times %d is %d" % (i, j, j * i))
    print("=========================")
# Using end='\t' to display with tabs as opposed to newlines:
for i in range(1, 13):
    for j in range(1, 13):
        print("%d times %d is %d" % (i, j, j * i), end='\t')
# one value for i per line, across within the same i value:
for i in range(1, 13):
    for j in range(1, 13):
        print("%d times %d is %d" % (i, j, j * i), end='\t')
    print("")  # move to next line using default \n value for print.  print("\n") would double space the lines
