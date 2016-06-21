#!/usr/bin/python3

# # Start with simple list:
# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
#
# # Work through the list, instructing user to buy all items:
# for item in shopping_list:
#     print("buy " + item)
# print('')
# # Use continue to skip the remainder of the for loop if certain condition is met.
# # Here, in Monty Python fashion, we don't like Spam:
# for item in shopping_list:
#     if item == 'spam':
#         continue  # if condition is met, move to the next item in the sequence (skips print command here)
#     print("buy " + item)
# print('')
# # Break stops processing the code block altogether, meaning future iterations are not completed.
# for item in shopping_list:
#     if item == 'spam':
#         print("Eww...  %s!? Buy your own groceries!" % item)
#         break  # You want spam?  Screw you, I'm not buying anything for you.
#     print("buy " + item)
# print('')

meal = ["egg", "bacon", "spam", "sausages"]  # list some items

# using break to drop to higher loop; to define what happens if a break condition is not met, we use else
# If spam is not part of the meal, then we order it
eww = ''
for item in meal:
    if item == 'spam':
        eww = item
        break
    else:
        print("I'll have a plate of that then, please")
if eww == 'spam':
    print("Couldn't I have something without spam in it?")


