print("Please enter a line of characters")
line = input()
lower_case_counter = 0
for curr_chr in line:
    if (ord(curr_chr) == 65):
        lower_case_counter += 1
    print("You have, " + str(lower_case_counter) + " , lowercase letters.")
        
        
