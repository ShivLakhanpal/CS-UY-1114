print("BMI = Body Mass Index and equals your weight divided by the square of your height")

weight = float(input("Please enter weight in kilograms: "))
height = float(input("Please enter height in meters: "))

BMI = (weight)/(height**2)

if (BMI < 18.5):
    print("Your BMI is: " + str(BMI) + " Since it is lower than 18.5, you are UNDERWEIGHT")
elif (18.5<=BMI<=24.9):
    print("Your BMI is: " + str(BMI) + " Since it is between 18.5 and 24.9, you are NORMAL")
elif (25.0<=BMI<=29.9):
    print("Your BMI is: " + str(BMI) + " Since it is between 25.0 and 29.9, you are OVERWEIGHT")
elif (BMI >= 30.0):
    print("Your BMI is: " + str(BMI) + " Since it is greater than 30.0, you are OBESE")
    

