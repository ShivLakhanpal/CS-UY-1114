#PART II


#Question 1
def mycount(lst, item):
    count = 0
    for char in lst:
        if char == item:
            count += 1 
    return count


#Question 2
def myindex(lst, item):
    for index in range(len(lst)):
        if lst[index] == item:
            return index
        elif item not in lst:
            return -1
        

#Question 3        
def all_indices(lst, item):
    lst_2 = []
    for index in range(len(lst)):
        if lst[index] == item:
            lst_2.append(index)
        elif item not in lst:
            return -1
    return lst_2

#Question 4        
def remove_below_avg(lst):
    total = 0
    for num in lst:
        total += num
    average = total/len(lst)

    lst_2 = []
    for num in lst:
        if num > average:
            lst_2.append(num)
    return lst_2



def main():
    print(mycount([123, 'xyz', 'zara', 'abc', 123],123))
    print(myindex([123, 'xyz', 'zara', 'abc', 123],123))
    print(all_indices([123, 'xyz', 'zara', 'abc', 123],123))
    print(remove_below_avg([2, 3, 5, 1, -4, 8, 0, -1]))
main()
    

    
    
