word = input("Please enter a word: ")
lower = word.lower()
size = len(lower)
vowel_counter = 0
consonant_counter = 0



for i in range(0, size):
    if (lower[i] == "a" or lower[i] == "e" or lower[i] == "i" or lower[i] == "o" or lower[i] == "u"):
       vowel_counter += 1
    else:
        consonant_counter += 1
print(str(word) + " has " + str(vowel_counter) + " vowels and " + str(consonant_counter) + " consonants.")

    


     
    
    
















