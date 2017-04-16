#Shiv Lakhanpal
#svl238
#hw9.py




#Question 1


def max_abs_value(lst):
    print(max(abs(num) for num in lst))
    return

#Question 2

def find_all(lst, val):
    lst_2 = []
    for index in range(len(lst)):
        if lst[index] == val:
            lst_2.append(index)
    return lst_2

#Question 3

def reverse1(lst):
    lst1 = lst[::-1]
    return lst1

def reverse2(lst2):
    new_lst = lst2[::-1]
    return new_lst

def main():

    lst = [1,2,3,4,5,6] #Input any list of numbers in this
    rev = reverse1(lst)
    print("After reverse1, lst is:",lst,"and the returned list is:",rev)

    lst2 = [1,2,3,4,5,6] #Input any list of numbers in this
    rev_2 = reverse2(lst)
    print("After reverse2, lst2 is: ",rev_2)


#Question 4

#Encoder

def run_length_encoder(string):

    lst_enc = []    #Empty List
    count = 1
    char_before= ""
    
    for char in string:   #The current character in the inputed string
        
        if char != char_before:
            
            if char_before:
                
                lst_encoder = (char_before, count) #List that takes the previous character and the number of times in list
                lst_enc.append(lst_encoder)  #Adds the mini list to the final list
                                            
            count = 1
            char_before = char
    
        else:
            count = count + 1
    else:
        lst_encoder = (char, count)
        lst_enc.append(lst_encoder)
        
    return lst_enc

#Decoder
        
def run_length_decoder(lst_enc):

    new_string = ""

    for (char,count) in lst_enc:

        new_string += char * count     #Multiplies number of times char is in list 
        
    return new_string





    


    
    
    


        
        
    
    




