#!/usr/bin/python3

# Replicating some earlier code.  Earlier, we used:
# cleanNumber = cleanNumber + number[i] to add each digit.  We can replace this statement using augmented assignment:
number = "9,223,098,000,111,458,123"
cleanNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanNumber += number[i]

newNumber = int(cleanNumber)
print("The number is {}".format(newNumber))


x = 23
print(x)
x += 1
print(x)
x -= 4
print(x)
x *= 5
print(x)
x /= 2.32
print(x)
x **= 3
print(x)
print("The resulting number of all these calculations, {0}, is {1} digits long.".format(x, len(str(x))))
