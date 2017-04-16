

n = int(input("Please enter a positive integer n and it will print out the Roman numeral: "))
roman = ""

if ((n // 1000) == 1):
    roman += "M"
if ((n // 500) == 1):
    (n // 500) >= 1
    i = n // 500
    roman += "D" * i
if ((n // 100) == 1):
    (n // 100) >= 1
    i = n//100
    roman += "C" * i
if ((n // 50) == 1):
    (n // 50) >= 1
    i = n//50
    roman += "L" * i
if ((n // 10) >= 1):
    i = n // 10
    roman += 'X' * i
    n -= i * 10
if ((n // 5) >= 1):
    h = n // 5
    roman += 'V' * h
    n -= h * 5
roman += 'I' * n

print('The Roman Numeral of ' , n , " is: " , roman)
