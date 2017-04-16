n = int(input("Please enter a positive integer n: "))

count = 2*n-1   #The count for top half of hour glass
count_2 = 2*n   #The count for bottom half of hour glass
space_1 = 0     #Space for top half
space_2 = 1     #Space for bottom half


#Top half of hour glass

for number in range(count, 0 , -2):
    num_line = ' ' * space_1 + number * "*" + '\n'
    space_1 += 1
    print(num_line)

#Top half of hour glass
    
for number in range(1, count_2, 2):
    num_line = ' ' * (n-space_2) + number * "*" + '\n'
    space_2 += 1
    print(num_line)

    


