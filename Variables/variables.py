#!/usr/bin/python3

# Python Complete Developer Course Section 5 Lectures 20 & 21: Variables (part 2 begins at line 44)

a = 12
b = 3

# add
print(a + b)
# subtract
print(a - b)
# multiply
print(a * b)
# divide (returns as a float, regardless of remainder)
print(a / b)
# divide, discarding remainder
print(a // b)
# calculate remainder
print(a % b)

# print numbers in a range (note: the final number is not printed)
for i in range(1, 5):
    print(i)

# # The following code produces an error: "TypeError: 'float' object cannot be interpreted as an integer".
# # Dividing always produces a float, and range() needs an integer value.
# for i in range(1, a / b):
#     print(i)

# Instead, the following should be used:
for i in range(1, a // b):
    print(i)

# complex expressions
# Operator precedence: multiplication/division occurs before addition/subtraction.  Left => right for operators in the
# subset. In the following, b / 3 happens first[1], then 4 * 12 [48].  Then a[12] + (b / 3)[1] = 13 - 48 = -35.0 (float
# not integer because division was involved). Also note that variables and hard values can be mixed freely:
print(a + b / 3 - 4 * 12)

# Parentheses can be used to override the default order of operations.  The following calculates the same equation in
# strict left => right order regardless of normal operation order
print((((a + b) / 3) - 4) * 12)

# Begin Lecture 21: Variables pt. 2
# The same results as above can be obtained through use of intermediate variables.  For instance:
c = a + b
d = c / 3
e = d - 4
print(e * 12)

# Data Type: Strings
parrot = "Norwegian Blue"
print(parrot)

# A [bracketed] number after the variable name will return the character in that position.  Remember that numbering
# starts with zero, so in the below example, the value of [3] indicates the FOURTH position.
print(parrot[3])

# Negative numbers work as well.  The value [-1], for example, will return the last character in a string, [-2] the
# second to last, and so on.
print(parrot[-1])

# A colon is used to define a range (slice) of characters to be displayed (remembering that we start with zero)
print(parrot[0:6])

# If starting at the beginning of the string, the first 0 is assumed, so not necessary to include
print(parrot[:6])

# Likewise, omitting the second number will continue until the end of the string
print(parrot[6:])

# A second colon indicates counting in steps.  For example, [0:6:2] will display every OTHER character from [0:6],
print(parrot[0:6:2])

# While [0:6:3] will display every THIRD:
print(parrot[0:6:3])

# Omitting the second number [n::n] will work until the end of the string.  In the following, we start with the first
# comma, in position 1, then print every 4th character (just the commas) until the end of the string.
number = '4,567,123,067,111,404,765'
print(number[1::4])

# The following starts with position zero, and prints every third character.  Due to the space after each comma,
# this prints just the numbers in this example
numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::3])

# Concatenate strings
string1 = "he's "
string2 = "probably "
string3 = "pining"
print(string1 + string2 + string3)

# Multiply strings
print("Hello " * 5)

# # Order of operations matters here too; The following fails with
# # TypeError: Can't convert 'int' object to str implicitly
# print("Hello" * 5 + 4)

# ...because ("Hello" * 5) converts to a string of Hello's, which you can't add an integer to.  Instead, use
print("Hello" * (5 + 4))

# "In" operator true/false
today = "monday"
print("day" in today)
print("mon" in today)
print("fri" in today)
print("parrot" in "fjord")

