#!/usr/bin/python3

# Python Complete Developer Course Section 5 Lecture 22: String Formatting

# Calling for the value of a variable in a print string
age = 38

# # The following will not work, producing the following error message:
# # TypeError: Can't convert 'int' object to str implicitly
# print("I am " + age + " years old")

# Instead, we need to use the str() function to convert the numerical value into a string
print("I am " + str(age) + " years old")

# Replacement fields
print("I am {0} years old".format(age))

# With only one variable, this isn't substantially better, but makes more sense with more data
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, and {7} ".format(31, "January", "March", "May",
      "July", "August", "October", "December"))

print("""January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July:{2}
August:{2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28, 30, 31))

# String formatting operators: deprecated in python 3
# %d = data, %s = string
print("My age is %d years" % age)
print("My age is %d %s, %d %s" % (age, "years", 6, "months"))

# Number after % indicates how much space should be allowed in the output.  A period after that, followed by a number,
# indicates to how many significant digits it should be calculated
for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" % (i, i ** 2, i ** 3))

print("Pi is approximately %12.50f" % (22 / 7))

# Back to replacement fields in comparison.  Number after the colon is padding.  < operator uses left justification
for i in range(1, 12):
    print("No. {0:2} squared is {1:<4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

# Precision is noted after a period, as in SFO
print("Pi is approximately {0:12.50}".format(22 / 7))

# The example on lines 22-33 shows how replacement fields allow for more control than string formatting operators.
# With SFO, each value can only be used once, so any repetitive data will require extra fields.
# Replacement fields allow you to address a particular value in a dataset as often as is necessary by invoking the
# position of the desired data.
# On sets that are in order (like existing python2 sources will have with SFO), leaving the array position blank {} will
# call the data in order.

for i in range(1, 12):
    print("No. {:2} squared is {:4} and cubed is {:4}".format(i, i ** 2, i ** 3))
