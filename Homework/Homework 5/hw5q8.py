print("Please enter a positive integer: ")
n = int(input())
num_count = 1


for line_number in range(1, n+1):
    num_step = (' '*(n - line_number))
    print(num_step, end = '')

    for number in range(1,line_number+1):
        print(number, end = '')
        
    num_count += 1
    print()


#I wasn't able to keep the structure the same when n was greter than 9.
    #After you grade this can you let me know how this is done.
    #Thank you :)
