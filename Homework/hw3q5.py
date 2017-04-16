import math
import turtle

print("Please enter lengths of a triangle's sides")

length_one = float(input("Length of first side: "))
length_two = float(input("Length of second side: "))
length_three = float(input("Length of third side: "))

if (length_one == length_two and length_two == length_three):
    turtle.right(0)
    turtle.forward(length_one)
    turtle.right(120)
    turtle.forward(length_two)
    turtle.right(120)
    turtle.forward(length_three)
    print(str(length_one) + " , " + str(length_two) + " , " + str(length_three) + " form an equilateral triangle")   
elif (length_one == length_two and length_three == length_one*math.sqrt(2)):
    turtle.right(0)
    turtle.forward(length_one)
    turtle.right(120)
    turtle.forward(length_two)
    turtle.right(120)
    turtle.forward(length_three)
    print(str(length_one) + " , " + str(length_two) + " , " + str(length_three) + " form an isoceles right triangle")
elif (length_one == length_two):
    turtle.right(0)
    turtle.forward(length_one)
    turtle.right(120)
    turtle.forward(length_two)
    turtle.right(120)
    turtle.forward(length_three)
    print(str(length_one) + " , " + str(length_two) + " , " + str(length_three) + " form an isoceles triangle")
elif(length_one != length_two and length_two != length_three):
    turtle.right(0)
    turtle.forward(length_one)
    turtle.right(120)
    turtle.forward(length_two)
    turtle.right(120)
    turtle.forward(length_three)
    print(str(length_one) + " , " + str(length_two) + " , " + str(length_three) + " form a scalene triangle")


