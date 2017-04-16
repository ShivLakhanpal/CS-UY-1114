input("Please enter a positive integer: ")
print("End the statement with the word 'done': ")
sequence_sum = 0
sequence_length = 0
curr_num = 1
seen_done = False

while (seen_done == False):
    curr_input = input()
    if(curr_input == 'done'):
        seen_done = True
    else:
        
        curr_num = int(curr_input)*curr_num
        sequence_sum += curr_num
        sequence_length += 1
if(sequence_length == 0):
    print("Empty sequence so no average")
else:
    average = (curr_num)**(1/sequence_length)
    
print("The average of the numbers is " , average)


#Itay Tal showed us how to do this in class, mine is a different variation.
