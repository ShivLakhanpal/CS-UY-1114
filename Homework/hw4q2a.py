#2a

print("----------Problem 2a----------")

print("Please enter a character: ")
char = input()
index = 0
curr_chr = char[index]

while (char[0] != "reset"):
    
    if (char[0].islower() == True):
        print(char, "is a lower case letter.")
    elif (char[0].isdigit() == True):
        print(char, "is a digit.")
    elif (char[0].isupper() == True):
        print(char, "is an upper case letter.")
    else:
        print(char, "is a non-alphanumeric character.")
        
    print("Please enter a character: ")
    char = input()
    

