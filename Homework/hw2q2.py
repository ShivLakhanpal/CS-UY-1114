number = int(input("Please enter a 3-digit number: "))


digit_1 = number % 10
digit_2 = number // 100

digit3 = number // 10

digit_3 = digit3 % 10

sum_digit = digit_1 + digit_2 + digit_3


print("The sum of the digits is " + str(sum_digit))
                 



