
from random import randint

#1

def writeName(filename, firstName, lastName):
    
    out_file = open("writeNameTest.txt", "w")
    print(firstName,lastName, file = out_file)
    
    out_file.close()



#2
def writeRandNumbers(filename,n):
    
    out_file = open(filename, 'w')
    
    for number in range(n):
        number = randint(1,100)
        print(number , file = out_file)
        
    out_file.close()
  
#3
def sumColumn(filename):
    
    in_file=open(filename,'r')

    total=0
    
    for column in in_file:
        number = str(column)
        number = int(number)
        total += number
        
    in_file.close()
    
    return total

def main():
    
    filename = input("Enter file name: ")
    n = int(input("Enter integer for n: "))
    writeRandNumbers(filename, n)
    total = sumColumn(filename)
    print("Total Sum is:", total)
    
main()

#4

def html_table_generator(file_name):
    
    in_file=open(file_name, 'r')
    
    print('<DOCTYPE html>')
    print('<html>')
    print('')
    print('<table>')
    print(' ','<tr>')
    
    heading = in_file.readline().strip().split(',')
    
    for element in heading:
        print('  ','<th>', end='')
        print(element, end='')
        print('</th>')
    print(' ','</tr>', sep=' ')
    
    for line in in_file:
        lst=line.strip().split(',')
        print(' ','<tr>')
        
        for elem in lst:
            print('  ','<td>', end='')
            print(elem, end='')
            print('</td>')
        print(' ','</tr>',sep=' ')
    print('</table>')
    print('')
    print('</html>')

    in_file.close()


def main():
    
    file_name = input('Please enter file name: ')
    html_table_generator(file_name)
    
main()


