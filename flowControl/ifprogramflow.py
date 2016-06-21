# #!/usr/bin/python3
# # name = input("Please enter your name: ")
# # # Convert input from string to integer using int()
# # age = int(input("How old are you, {0}? ".format(name)))
# # print(age)
# #
# # if age >= 18:
# #     print("You are old enough to vote")
# # else:
# #     print("You are not yet old enough to vote. Please come back in {0} years.".format(18 - age))
#
# print("Please guess a number between 1 and 10: ")
# guess = int(input())
# winner = 5
# #
# #
# # if guess > winner:
# #     print("Too high, Einstein.  One more chance: ")
# #     guess = int(input())
# #     if guess == winner:
# #         print("You Win.  Congratulations!")
# #         print("Please claim your winnings in person on Omicron Persei 8")
# #         print("...have fun with that.")
# #     else:
# #         print("Too Bad.  Maybe you're just not smart?")
# # elif guess < winner:
# #     print("Too low, jackass.  I'll give you one more chance: ")
# #     guess = int(input())
# #     if guess == winner:
# #         print("You Win.  Congratulations!")
# #         print("Please claim your winnings in person on Omicron Persei 8")
# #         print("...have fun with that.")
# #     else:
# #         print("Too Bad.  Maybe you're just not smart?")
# # else:
# #     print("Whaddya know? I didn't think you had it in you.")
# #     print("Congratulations, you guessed a number.  You probably feel smart,")
# #     print("but you really shouldn't. 1 out of 10 ain't exactly lottery odds")
#
# # A much cleaner version of the above guessing game, with guess > 10 error condition
#
# if guess != winner:
#     if guess > 10:
#         print(
#             """{} is between 1 and 10 now?  Why wasn't I notified?
# Maybe you would have learned something in Elementary school
# if you weren't such an asshole.  Now pick again: """.format(guess))
#
#     elif guess < 5:
#         print("Too low, jackass.  I'll give you one more chance: ")
#     else:
#         print("Too high, Einstein.  One more chance: ")
#
#     guess = int(input())
#
#     if guess == winner:
#         print(
#             """You Win.  Congratulations!)
# Please claim your winnings in person on Omicron Persei 8
# ...have fun with that.""")
#     else:
#         print("Too Bad.  Maybe you're just not smart?")
# else:
#     print("Whaddya know? I didn't think you had it in you.")
#     print("Congratulations, you guessed a number.  You probably feel smart,")
#     print("but you really shouldn't. 1 out of 10 ain't exactly lottery odds")
#
# # Begin lecture 26.  commenting above.

age = int(input("How old are you? "))

# if (age >= 16) and (age <= 54):
if 16 <= age <= 65:
    print("Have a good day at work")

print("""False: {0}
None: {1}
0: {2}
0.0: {3}
empty list []: {4}
empty tuple (): {5}
empty string '':{6}
empty string "": {7}
empty mapping {{}}: {8}
""".format(False, bool(None), bool(0), bool(0.0), bool([]), bool(()), bool(''), bool(""), bool({})))

parrot = "Norwegian Blue"
letter = input("enter a letter: ")


if letter not in parrot:
    print("I don't need that letter ")
else:
    print("Give me a {}, Bob!".format(letter))
