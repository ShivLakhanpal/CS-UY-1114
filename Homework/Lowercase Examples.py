print ("Please enter a line of characters")
line = input()
lower_case_counter = 0
index = 0
while (index < len(line)):
    curr_chr = line[index]
    if(curr_chr.islower() == True):
        lower_case_counter += 1
    index += 1
print("You have " + str(lower_case_counter) + " lowercase letters")
      
