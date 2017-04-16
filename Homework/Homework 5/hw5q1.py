pos_int = int(input("Please enter a positive integer: "))
odd_counter = 1

for i in range(0,pos_int):
    if int(i) > 0:
        print(odd_counter)
        odd_counter += 2
print(odd_counter)
