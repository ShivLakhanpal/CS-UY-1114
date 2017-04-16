def list_of_train_stops(name_of_file):
    dict_train = {} #Created a dictionary to add all train stops in each train line
    
    data_file = True
    while data_file:
#using a try and except function to instruct the computer to
#know if correct folder is inputed and correct data
        try:
            
            data_train = open(name_of_file, "r")
            data_train.readline()
            
            for line_str in data_train:
                
                if line_str != "\n":    #I said line_str != '\n' so I could differentiate between the empty lines and the lines with data
                    
                    line_str = line_str.strip()
                    
                    final_line = line_str.split(",") #Split the function based on commas

                        #Instead of cleaning out the file, I targeted the column I had to use for this assignment i.e.
                        #train_line, stop_id, stop_name

                    
                    first_column = final_line[0]  #This is the first column
                    line_train = first_column[0]
                    name_train = final_line[2]    #Second Column

                    #Next line of code is if/else statement to add the train
            #lines to the key which is dict_train

                    
                    if line_train in dict_train:
                        
                        if name_train not in dict_train[line_train]:
        
                            dict_train[line_train].append(name_train)  #Adds the data to train stops
                    else:
                        
                        dict_train[line_train] = [name_train]
            
            data_train.close()
            
            return dict_train   #Return dictionary with all the train stops    
        except IOError:
            print("Error: Could not open that file. Please try again.") #If input is invalid/incorrect try again

def main():
    file_stops = list_of_train_stops("Ye.csv")
    train = input("Please enter a train line, or 'done' to stop: ")
    
    while train != "done":
        #This continues the loop forever if the user doesn't enter done
        if train in file_stops:
            print(train,"line:",end = ' ')
            
            space = ""
            
            for element in file_stops[train]:      #This reads the element in the train file
                
                space += element + ", "
                
            print(space,"\n")

            
        else:
            print("The line you entered does not exist\n")   
        #If the user entered something incorrectly ask them to input a new train line            
        
        train = input("Please enter a train line again and please enter 'done' to stop the program: ")

main()
                
                
                
        
    
    
                    

