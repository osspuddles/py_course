#!/usr/bin/python3
# ipAddress = input("Please enter an IP address: ")
# print(ipAddress.count("."))

# a list
parrotList = ["not pinin'", "no more", "a stiff", "bereft of life"]
for state in parrotList:
    print("This parrot is " + state)
print('')
# add to the list with .append
parrotList.append("an ex-parrot")
for state in parrotList:
    print("This parrot is " + state)
print('')


even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# this list will be out of order, as the 2 lists are just glued together
numbers = even + odd
print(numbers)

# adding .sort function
numbers = even + odd
numbers.sort()
print(numbers)

# same thing, creating an object using sorted
numbers = even + odd
print(sorted(numbers))

