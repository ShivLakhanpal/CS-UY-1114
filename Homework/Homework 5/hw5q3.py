
lowercase_string = input("Please enter a string of lowercase letter: ")
lowercase_string_lower = lowercase_string.lower() # Make sure input is always lowercase

increasing_string = True    #Assigning an increasing string to True

for i in range(len(lowercase_string)-1):
    if (lowercase_string[i] >= lowercase_string[i+1]):
        increasing_string = False
if (increasing_string == True):
        print(lowercase_string_lower,"is increasing")
else:
        print(lowercase_string_lower,"is not increasing")
          
        
    

    
