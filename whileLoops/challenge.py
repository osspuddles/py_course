#!/usr/bin/python3

import random

highest = 1000
answer = random.randint(1, highest)
guess = ''
tries = 0
while guess != answer:
    if tries > 2:
        print("Please guess a number between 1 and {}: (0 to quit.)".format(
                highest))
    else:
        print("Please guess a number between 1 and {}: ".format(highest))
    guess = int(input())

    if guess == 0:
        guess = answer
        tries = 8675309
    elif guess == answer:
        tries += 1
    elif guess > highest or guess < 0:
        print("""I said between 1 and {0}, didn't I?
         Since when is {1} between 1 and {0}?
         Try again, smartass.""".format(highest, guess))
        tries += 1
    elif guess > answer:
        print("Sorry, too high.  try again :")
        tries += 1
    else:
        print("Sorry, too low.  try again:")
        tries += 1

else:
    if tries == 1:
        print("Wow.  First try.  Good guess!")
    elif tries == 8675309:
        print("I get it.  It's really not that fun. I'd probably quit too. \n"
              "If you're interested, the number was {}".format(answer))
    else:
        print("""Congratulations!
        You guessed the number in {} tries!""".format(tries))
