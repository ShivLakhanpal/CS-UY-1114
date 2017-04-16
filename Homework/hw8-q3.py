#Shiv Lakhanpal
#svl238
#hw8-q3.py

'''This code prints out a pine-tree when the user is confronted with several inputs such as
the number of lines and the character the pine-tree will consist off'''


#1

def print_shifted_triangle(n, m, symbol):
    space = " "
    amount_of_char = 1
    amount_of_spaces = n-1
    for i in range(1, n+1):
        line = space * m + space * amount_of_spaces + symbol * amount_of_char
        print(line)
        amount_of_char += 2
        amount_of_spaces -= 1
        
    
#2

def print_pine_tree(n, symbol):
    for i in range(2,n+2):
        print_shifted_triangle(i,n-1,symbol)
        n -= 1
#3
        
def main():
    n = int(input("Please enter an integer for number of lines: "))
    symbol = input("Please enter a character: ")
    pine_tree = print_pine_tree(n,symbol)
main()

    
