#Shiv Lakhanpal
#svl238
#hw10.py

'''These problems mainly focused on lists. the first question asked us the switch
order of the list whenever a user inputed a list. The second question asked
us to shuffle a list depending on the user inputing an integer n. The second question
I had to add the indexes of each list. The third question we had to create several lists
depending on how many values were in one list. The last question was a menu question where
we asked the user to input the number of items in the menu.'''

import random

#Question 1a

def create_permutation(lst):
    random_list = []
    while(len(lst) > 0):
        position = random.randrange(0,len(lst))
        random_list.append(lst.pop(position))
    return random_list


#Question 1b

def create_permutation(lst):
    random_list = []
    while(len(lst) > 0):
        position = random.randrange(0,len(lst))
        random_list.append(lst.pop(position))
    return random_list


def main():
    n = int(input("Please enter integer: "))
    lst = []

    for x in range(1,n+1):
        lst.append(x)
        random.shuffle(lst)
    print(create_permutation(lst))
   
main()
    

#Question 2

def add_list(lst1, lst2):
    lst3 = []
    if len(lst1) != len(lst2):
        print("Lists are different lengths")
        return
    else:
        for index in range(len(lst1)):
            sum_index = lst1[index] + lst2[index]
            lst3.append(sum_index)
    return lst3

#Question 3

def create_prefix_lists(lst):

    list_final = []
    list_prefix = []
    list_final = ([])
    for previous_char in range(len(lst)):
        list_prefix = []

        for char in range(0,(previous_char+1)):
            
            list_prefix.append(lst[char])
        list_final.append(list_prefix)
        
    return list_final

#Question 4:


#4a

def read_menu():
    
num_items = int(input("How many items on the menu? "))

final_menu_list = []

for pos in range(n):
    item = input("Please enter an item in the form of 'name:price: ")
    list_item = final_menu_list.split(":")
    t_item = tuple(list_item)
    list_item[1] = float(list_item[1])
    final_menu_list.append(t_item)
return final_menu_list

#4b

print("Please complete your order by entering which items you would like and write done to submit order: ")

user_input = False
final_order = []

while user_input == False:
    input_c = input()
    
    if input_c == "done":
        input_c = True
    else:
        final_order.append(input_c)
return final_order

#4c



#4d

def tip(price):
    tip = 0.15*price
    return tip

def tax(price):
    tax = 0.085*price
    return tax
    





