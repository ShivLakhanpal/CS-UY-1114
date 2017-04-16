import math

print("We will solve for x using the linear equation ax^2+bx+c = 0")
a = float(input("Please enter an integer value for a: "))
b = float(input("Please enter an integer value for b: "))
c = float(input("Please enter an integer value for c: "))



if(a == 0 and b == 0 and c != 0):
    print("The equation has an no solution")
elif(a < 0 and b < 0 and c < 0):
    print("The equation has a single real solution")
elif(a > 0 and b > 0 and c > 0):
    print("The equation has a single real solution"ss)
elif(a == 0 and b ==0 and c == 0):
    print("This equation has an infinite number of solutions")
elif(b**2-(4*a*c) < 0):
    print("This equation has no real solution")
elif(b**2-(4*a*c) == 0):
    output = (-b/(2*a))
    print("This equation has a single real solution of , " + str(output))
elif(b**2-(4*a*c) > 0):
    output_1 = (-b + math.sqrt(b**2-(4*a*c)))/(2*a)
    output_2 = (-b - math.sqrt(b**2-(4*a*c)))/(2*a)
    print("This equation has a two real solutions of %.2f"%output_1 ,"and %.2f"%output_2)
