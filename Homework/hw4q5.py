#5

print("----------Problem 5----------")

potential_password = input("Please make a password that is at least eight characters long and contains at least one uppercase letter: ")
upper_case_counter = 0
digit_counter = 0
non_alpha_counter = 0
for curr_char in potential_password:
    if (curr_char.isupper()):
        upper_case_counter += 1
    elif (curr_char.isdigit()):
        digit_counter += 1
    elif(33 <= ord(curr_char) <= 47):
        non_alpha_counter += 1
    elif (58 <= ord(curr_char) <= 64):
        non_alpha_counter += 1
    elif (91 <= ord(curr_char) <= 96):
        non_alpha_counter += 1
    elif(123 <= ord(curr_char) <= 126):
        non_alpha_counter += 1
        
    
    
if (len(potential_password) >= 8 and upper_case_counter > 0):
    print("Valid Password")
elif(len(potential_password) >= 8 and digit_counter > 0):
    print("Valid Password")
elif(len(potential_password) >= 8 and non_alpha_counter > 0):
    print("Valid Password")
else:
    print("Invalid Password")

potential_password = input('Please make a password that is at least six characters long and contains at least one uppercase letter: ')
upper_case_counter = 0
digit_counter = 0
non_alpha_counter = 0

