n = int(input("Please enter the length of a sequence: "))
curr_product = 1

for i in range(1,n+1):
    curr_product = curr_product*float(input("Please enter a positive integer: "))
geo_mean = (curr_product)**(1/n)

print("The average of the numbers is " , geo_mean)
