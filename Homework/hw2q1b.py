pounds = float(input("Please enter weight in pounds: "))
inches = float(input("Please enter height in inches: "))

weight = float(pounds*0.453592)
height = float(inches*0.0254)

BMI = (weight)/(height**2)

print("The BMI is: " + str(BMI))
