#1:

input_str = input("Please enter a string of 0s and 1s: ")
current_position = 0
print_str = "Your string has: \n"

while(current_position < len(input_str)):
    flag = input_str[current_position]
    counter = 0
    while(current_position < len(input_str) and flag == input_str[current_position]):
        counter += 1
        current_position += 1
    print_str += str(counter) + " " + flag + "'s \n"
print(print_str)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       

#2:
import random

rand_num = random.randint(1,100)
guess = int(input("Guess the number between 1 and 100 I am thinking of: "))

while(guess != rand_num):
    if (guess > rand_num):
           print("Wrong guess")
           guess = int(input("My number is smaller. Guess again: "))
    if (guess < rand_num):
        print("Wrong guess")
        guess = int(input("My number is bigger. Guess again: "))
print("Congrats you guessed my number!")
