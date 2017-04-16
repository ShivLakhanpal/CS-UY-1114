#Problem 1:

print("---------Problem 1----------")


n = int(input("Enter a number here: "))
factorial = 1
for num in range(1,n+1):
    factorial = num * factorial
print("The factorial of" ,num, "is", factorial)



print("---------Problem 2----------")

string = input("Please enter a string: ")
string_2 = " "

for char in string:
   if char.islower() == True:
      char = char.upper()
      string_2 += char
   else:
      char = char.lower()
      string_2 += char
print("The new string is: ",string_2)


print("---------Problem 3----------")

first_name = input("Please enter name 1: ")
second_name = input("Please enter name 2: ")

space_index = first_name.find(' ')
space_index_2 = second_name.find(' ')

if first_name[:space_index-1] == second_name[space_index_2 +1:] and first_name[space_index + 1:]\
   == second_name[:space_index_2]:
   print("The two names are equal!")
else:
   print("The two names are the same.")

print("----------Problem 3----------")

string = input('Please enter an expression: ')
curr_chr = input('Please enter a letter: ')
counter = 0

while(curr_chr == '' ):
    counter += 1
print ('Letter',curr_chr,'appears',counter,'times in your string.')
