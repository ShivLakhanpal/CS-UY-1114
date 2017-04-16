word = input("Please enter a word: ")
lower_word = word.lower()

vowel_counter = 0
consonant_counter = 0


if lower_word or "a" in word:
    vowel_counter += 1

if "E" or "e" in word:
    vowel_counter += 1

if "I" or "i" in word:
    vowel_counter += 1

if "O" or "o" in word:
    vowel_counter += 1

if "U" or "u" in word:
    vowel_counter += 1

else:
    consonant_counter += 1

print(str(word) + " has " + str(vowel_counter) + " vowels and " + str(consonant_counter) + " consonants ")
