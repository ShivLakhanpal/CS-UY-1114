'''n = int(input("Please enter a positive integer n: "))
i = 0
s = i//10
m = i//100
junk_counter = 0

while (i < n):
    i +=2
    if (i//10 == 1 or i//10 == 3 or i//10 == 5 or i//10 == 7 or i//10 == 9):
        junk_counter += 1
    else:
        print(i)'''

n = int(input("Please enter a positive integer: "))

for line_number in range(1, n+1):
    line = "*" + '\t'  * n
    print(line)

