'''
Shiv Lakhanpal
svl238
hw7q1.py

This code is a Ceaser Cipher which asks the user to input a word and enter a
a shift, and depending on the shift it changes the original word and switches
it to an encrypted word based off the shift.
'''



original_word = input("Please enter word: ")
shift = int(input("What shift should we apply: "))
enc_string = ""

for character in original_word:
    if character.isupper() == True:
        new = ord(character) + shift
        if new >= 91:
            new -= 26
        enc_string += chr(new)
    elif character.islower():
        new = ord(character) + shift
        if new >= 123:
            new -= 26
        enc_string += chr(new)
    elif character.isupper() == False and character.islower() == False:
        new = character
        enc_string += new
 
print("The encoded word is:",enc_string)

