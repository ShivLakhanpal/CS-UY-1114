'''
Shiv Lakhanpal
svl238
hw7q3.py

This code asks the user to guess a number between 1 and 100, and the user
only has 5 chances to guess the number and the code also gives the range in
which the number lies in.
'''



import random

num_random = random.randint(1,100)
guess_count = 0
chance_count = 5
guess = int(input("Guess the number between 1 and 100! Try to guess it: "))

while(guess != num_random):
    if (guess > num_random):
           chance_count -= 1
           guess = int(input("Wrong Guess! Guess in range " + str(guess-18) + " to " + str(guess-1) + " You have " + str(chance_count) + " chances: "))
           guess_count += 1
    if (guess < num_random):
        chance_count -= 1
        guess = int(input("Wrong Guess! Guess in range " + str(guess+1) + " to " + str(100) + " You have " + str(chance_count) + " chances: "))
        guess_count += 1
    if chance_count == 0:
        print("Sorry no more chances, you failed to guess my number")
        break
    else:
        if (guess == num_random):
            print("Congrats you guessed my number in", guess_count,"guesses")

