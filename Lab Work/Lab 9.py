#Part 2

#1a

def count(lst, item):
    count  = 0
    for char in lst:
        if (char == item):
            count += 1
    return count

#1b

n = int(input("Please enter an integer: "))
counter = 1
lst = []

while(counter <= n):
    lst.append(2**counter)
    counter += 1
print(lst)

#1c

def find_min_index(lst):
    minimum = 0
    for num in lst:
        if (1 < minimum):
            minimum = 1
    return minimum


#1d

def circular_shift_list1(lst, k):
    lst2 = []
    for index in range(len(lst)):
        count = k - ((len(lst) - 1) - index) - 1
        lst2.append(count, lst[index])
        lst2[index+k] = lst[index]
    return lst2

#1e
def circular_shift_lst2(lst):
    n=int(input("Please enter number of elements to shift: "))
    first_part=lst[n:]
    second_part=lst[0:n]
    lst=first_part+second_part
    return lst

def main():
    lst=[]
    n=int(input("Please enter length of list: "))
    for i in range(n):
        element=input("Please enter element of list: ")
        lst.append(int(element))
    res_lst=circular_shift_lst2(lst)
    print(res_lst)
main()

#2

def get_Common_Ele(list1,list2):
    list_complete = []
    if (len(list1) > len(list2)):
        for num in list2:
            for num2 in list1:
                if(num == num2):
                    list_complete.append(num)
    else:
        for num in list1:
            for num2 in list2:
                if (num == num2):
                    list_complete.append(num)
    return list_complete

#3a

def power():
	list1 = [2,3,4,5,6]
	list2 = ""
	for i in list1:
		print (i ** 2)

#3b

def main():
    lst=[]
    element=''
    while element!='done':
        element=input('Please enter element of list: ')
        if element=='done':
            break
        element=int(element)
        element=element**2
        lst.append(element)
    total=sum(lst)
    average=total/len(lst)
    print('The average of the squares of the list of numbers is: ', average )
main()




