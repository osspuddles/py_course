# #!/usr/bin/python3
#
# # Example of a simple for loop:
# for i in range(10):
#     print("i is now {}".format(i))
#
# # Doing the exact same thing in a while loop actually requires more lines
# # First, we have to initialize the variable.  This is not required in a for
# # loop as the explicit range is specified:
# i = 0
# # The next part is quite similar:
# while i < 10:
#     print("i is now {}".format(i))
#     # But then we need one more step.  We need to manually increment the value
#     # of i, or else the condition can never be false:
#     i += 1
#
# # An example of an adventure game in which you have to choose a direction:
# available_exits = ["east", "north-east", "south"]
#
# chosen_exit = ''
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit == "quit":
#         print("Game Over")
#         break
# else:
#     print("What a pain in the ass, eh?")

# A guessing game from a previous lesson, with randomness added:
import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())
if guess != answer:
    if guess > answer:
        print("Sorry, too high.  try again:")
    else:
        print("Sorry, too low.  try again:")
    guess = int(input())
    if guess == answer:
        print("You got it!")
    else:
        print("Sorry, the answer was {}. Better luck next time!".format(answer))
else:
    print("First try! Good job!")

