import math
import turtle

#1

print("----------Problem 1----------")

a = int(input("Please enter a non-zero value for the a-coordinate: "))
b = int(input("Please enter a non-zero value for the b-coordinate: "))

if (a > 0 and b > 0):
    print("coordinates (a,b) are located in the 1st quadrant")
elif(a < 0 and b > 0):
    print("coordinates (a,b) are located in the 2nd quadrant")
elif (a < 0 and b < 0):
    print("coordinates (a,b) are located in the 3rd quadrant")
elif (a > 0 and b < 0):
    print("coordinates (a,b) are located in the 4th quadrant")

#3

print("----------Problem 3----------")

old_phone = str(input("Please input the old NYU phone number: "))
new_phone = ("718-260-")

if  (new_phone == old_phone[0:8]):
    print("646-997-" + old_phone[8:])
else:
    print("This is not a valid old NYU SoE phone number.")


#4

print("----------Problem 4----------")

print("Please enter a color: either red, blue or green: ")
turtle_color = input()
print("Please enter the shape: triangle or square: ")
turtle_shape = input()
print("Please enter a size: ")
turtle_size = int(input())

if (turtle_shape == "triangle" and turtle_color == "red"):
    turtle.color("red")
    turtle.right(360)
    turtle.forward(turtle_size)
    turtle.right(120)
    turtle.forward(turtle_size)
    turtle.right(120)
    turtle.forward(turtle_size)
elif (turtle_shape == "triangle" and turtle_color == "blue"):
    turtle.color("blue")
    turtle.right(360)
    turtle.forward(turtle_size)
    turtle.right(120)
    turtle.forward(turtle_size)
    turtle.right(120)
    turtle.forward(turtle_size)
elif (turtle_shape == "triangle" and turtle_color == "green"):
    turtle.color("green")
    turtle.right(360)
    turtle.forward(turtle_size)
    turtle.right(120)
    turtle.forward(turtle_size)
    turtle.right(120)
    turtle.forward(turtle_size)
elif (turtle_shape == "square" and turtle_color == "red"):
    turtle.color("red")
    turtle.forward(turtle_size)
    turtle.left(90)
    turtle.forward(turtle_size)
    turtle.left(90)
    turtle.forward(turtle_size)
    turtle.left(90)
    turtle.forward(turtle_size)
elif (turtle_shape == "square" and turtle_color == "blue"):
    turtle.color("blue")
    turtle.forward(turtle_size)
    turtle.left(90)
    turtle.forward(turtle_size)
    turtle.left(90)
    turtle.forward(turtle_size)
    turtle.left(90)
    turtle.forward(turtle_size)
elif (turtle_shape == "square" and turtle_color == "green"):
    turtle.color("green")
    turtle.forward(turtle_size)
    turtle.left(90)
    turtle.forward(turtle_size)
    turtle.left(90)
    turtle.forward(turtle_size)
    turtle.left(90)
    turtle.forward(turtle_size)


#5
    
print("----------Problem 5----------")

word = input("Please enter another three word phrase: ")
one = word[0]
two = word[word.find(" ")+1]
word = word[(word.find(" ")+1):]
three = word[word.find(" ")+1]
print(one + two + three)
word1 = input("Please enter a three word phrase: ")
print(word1.upper())
word2 = input("Please enter another three word phrase: ")
print(str(ord(word2[0])) + " " + str(ord(word2[1])) + " " + str(ord(word2[2])))

#6

print("----------Problem 5----------")

potential_password = input('Please make a password that is at least six characters long and contains at least one uppercase letter: ')
upper_case_counter = 0
for curr_char in potential_password:
    if curr_char.isupper():
        upper_case_counter = upper_case_counter + 1

if len(potential_password) >= 6 and upper_case_counter > 0:
    print('Valid Password')
else:
    print('Invalid Password')

#7

print("----------Problem 7----------")

a = input("Please enter two positive integers seperated by a space: ")
number_one = a[0:a.find(' ')]
number_two = a[a.find(' ')+1:]
a_2 = str(number_one) + "+" + number_two + "=" + str(int(number_one) + int(number_two))
print(a_2)
                                                     

