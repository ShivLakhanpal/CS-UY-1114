#1

print(" ----------Problem 1------------")

number = int(input('Please enter an integer less than 100:'))
times_roman = ''

if ((number // 50) == 1):
    times_roman += "L"
    number -= 50
if ((number // 10) >= 1):
    i = number // 10
    times_roman += 'X' * i
    number -= i * 10
if ((number // 5) >= 1):
    h = number // 5
    times_roman += 'V' * h
    number -= h * 5
times_roman += 'I' * number

print('The Roman Numeral is: ' + times_roman)





#2

print(" ----------Problem 2------------")


first_length = int(input("Please enter the first shortest length: "))
second_length = int(input("Please enter the second biggest length: "))
third_length = int(input("Please enter the biggest length: "))

legs = ((first_length**2) + (second_length**2))
hypo = third_length**2

if (legs == hypo):
    print (str(first_length) + ', ' + str(second_length) + ', ' + str(third_length) + ', ' + "forms a right triangle ")
else:
    print ("Lengths do not form a right triangle")



#3
##################



#4

print(" ----------Problem 4------------")


print("We will solve for x using the linear equation ax+b = 0")
integer_a = int(input("Please enter an integer value for a: "))
integer_b = int(input("Please enter an integer value for b: "))

value_x = (-integer_b)/(integer_a)

if(integer_a == 0 and b != 0):
    print("The equation has an infinite number of solutions and " + "x = " + str(value_x))
elif(integer_a == 0 and b == 0):
    print("The equation has a unique solution and " + "x = " + str(value_x))
elif(integer_a > 0 and integer_b > 0):
    print("The equation has a single solution and " + "x = " + str(value_x))


#5

print(" ----------Problem 5------------")

name = input("Please enter your name: ")
grad_year = int(input("Please enter your graduation year: "))
current_year = int(input("Please enter the current year: "))

freshman = current_year + 4
sophomore = current_year + 3
junior = current_year + 2
senior = current_year + 1

if (grad_year == senior):
    print(name + " is a senior")
elif (grad_year == junior):
    print(name + " is a junior")
elif (grad_year == sophomore):
    print(name + " is a sophomore")
elif (grad_year == freshman):
    print(name + " is a freshman")



      
