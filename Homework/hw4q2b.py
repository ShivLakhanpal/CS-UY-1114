#2b


print("----------Problem 2b----------")



print("Please enter a character: ")
char = input()

while (char[0] != "RESET"):
    
    if (97 <= ord(char) <= 122 ):
        print(char, "is a lower case letter.")
    elif (48 <= ord(char) <= 57):
        print(char, "is a digit.")
    elif (65 <= ord(char) <= 90):
        print(char, "is an upper case letter.")
    elif (33 <= ord(char) <= 47):
        print(char, "is a non-alphanumeric character.")
    elif (58 <= ord(char) <= 64):
        print(char, "is a non-alphanumeric character.")
    elif (91 <= ord(char) <= 96):
        print(char, "is a non-alphanumeric character.")
    elif(123 <= ord(char) <= 126):
        print(char, "is a non-alphanumeric character.")

    print("Please enter a character: ")
    char = input()

        
