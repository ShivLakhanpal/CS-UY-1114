import math

print("----------Problem 1----------")

kg = int(input("Enter Kilograms:"))
pounds = int(kg * 2.20462)
remainder = (kg * 2.20462) - pounds
ounces = remainder * 16
print(str(kg) + " Kilograms is equal to " + str(pounds) + " pounds" + " and " + str(ounces) + " ounces")


#######

print('''

----------Problem 2----------''')



inches = int(input("Enter an integer value for inches:"))
feet = inches//12
inchesRes = inches % 12

print( str(inches) + " inches" + " equals to " + str(feet) + " feet" + " and " + str(inchesRes) + " inches")


######

print('''
----------Problem 3----------''')

radius = int(input("Enter an integer value for radius:"))
circumference = (2*math.pi*radius)
area = (math.pi*(radius**2))
print( "Circumference of the circle is " + str(circumference) + " and the area of the circle is " + str(area))

######

print('''
----------Problem 4----------''')

#Problem 4:

import turtle
turtle.right(120)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)

######


#Problem 5:

turtle.clear()
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)



#Problem 6:

print('Enter your year of birth:')
usersyear =int(input())
print('Enter your month of birth:')
usersmonth = int(input())
print('Enter your date of birth:')
usersdate = int(input())
print('Enter todays year:')
todaysyear = int(input())
print('Enter todays month:')
todaysmonth = int(input())
print('Enter todays date:')
todaysdate = int(input())
Usersageyear = (todaysyear*365 - usersyear*365)
Usersagemonths = (todaysmonth*30 - usersmonth*30)
Usersageday = (todaysdate - usersdate)

print('You are', Usersageyear//365, 'years old,', Usersagemonths//30, 'months old and',\
      Usersageday, 'days old.')







#Problem 7:

print('''
----------Problem 7----------''')

firstLengthFeet = int(input("Please enter the first length's feet:"))
firstLengthinches = int(input("Please enter the first length's inches:"))

secondLengthFeet = int(input("Please enter the second length's feet:"))
secondLengthinches = int(input("Please enter the second length's inches:"))

print("Their sum is: " + str(firstLengthFeet+ secondLengthFeet) + " feet " + str(firstLengthinches + secondLengthinches) + " inches")
    
                        








