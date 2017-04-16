#1a

print("Problem 1a: ")

    
n = 10

def fib(n):
     if n == 1:
         return 1
     elif n == 0:
         return 0            
     else:                      
         return fib(n-1) + fib(n-2)
print(fib(n-10),fib(n-9),fib(n-8),fib(n-7),fib(n-6),fib(n-5),fib(n-4),fib(n-3),fib(n-2),fib(n-1))
    


#1b

print("Problem 1b: ")

number = int(input("Please enter a number: "))

def fib(n):
   if n == 1:
      return 1
   elif n == 0:   
      return 0            
   else:                      
      return fib(n-1) + fib(n-2)
print("The", str(number)+"th", "Fibonacci number is:",fib(number))


#1c
print("Problem 1c: ")

def fib(n):
   if n <= 1:
       return n
   else:
       return(fib(n-1) + fib(n-2))

fib_seq = int(input("Please enter a number: "))

if fib_seq <= 0:
   print("Plese enter a positive integer")
else:
   print()
   for num in range(fib_seq):
       print(fib(num))

def find(some_string, substring, start, end):
    length = len(substring)
    index = end-length
    if length == 1:
        for curr in range(start,end):
            if some_string[curr: curr+length]==substring:
                return curr
                
            else:
                return 1
    if length>1:
        for i in range(0,index+1):
            if substring==some_string[i:i+length]:
                return i
#NUMERO 2B
def multi_find(some_string, substring, start, end):
    first=find(some_string, substring, start, end)
    if first==-1:
        return first
    if first>0:
        length=len(substring)
        index=end-length
        res=''
        for i in range(0,index+1):
            if substring==some_string[i:i+length]:
                res+=str(i)+','
        return res
    

def main():
    some_string = str(input("Enter string: "))
    substring = str(input("Enter substring: "))
    start = int(input("Enter a start: "))
    end = int(input("Enter an end: "))
    res = find(some_string, substring, start, end)
    print(res)
    res = multi_find(some_string, substring, start, end)
    print(res)
    
main()
