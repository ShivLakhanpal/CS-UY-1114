#1

def writeName(filename, firstName, lastName):
    
    out_file = open("writeNameTest.txt", "w")
    print(firstName,lastName, file = out_file)
    
    out_file.close()

#2

import random

def writeRandNumbers(filename, n):
    
    out_file = open("lab11_q2.txt", "w")

    for n in range(1,n+1):
        print(random.randint(1,100), file = out_file)

    out_file.close()
    

#3


def sumColumn(filename):
    
    out_file = open("lab11_q3.txt", "w")
    total = 0
    for n in range(1,n+1):
        print(random.randint(1,100), file = out_file)

    out_file.close()


#4
    
