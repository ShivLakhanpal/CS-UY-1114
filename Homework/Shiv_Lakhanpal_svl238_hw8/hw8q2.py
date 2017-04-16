
#Shiv Lakhanpal
#svl238
#hw8q2.py

'''This code consists of 4 parts, a, b, c, d. The first part asked me to create
create a function, given a phrase and returns the first word in that phrase.
The second part asked me to return that phrase, created in part a, whilst eliminating the first word.
The third part asked me to reverse the words of the phrase without the first word.
Lastly, the fourth and final part asked the user to input a phrase and it would print all the parts described above.'''

#I was unable to fully complete 2c, I was confused on how to do it. After you grade this homework can you
#explain to me on how to do it. Thanks :)



#Question 2a

space = ' '
mini_space = ''

def word(phrase):
    index = phrase.find(space)
    phrase_first_word = phrase[:index]
    return phrase_first_word


#Question 2b


def phrase_minus_first(phrase):
    
    index = phrase.find(space)
    phrase_without_first = phrase[index+1:]
    return phrase_without_first 


#Question 2c



def reversed_phrase(phrase):

    count_1 = 1
    for char in phrase:
        if(char == space):
            count_1 += 1
    count_2 = 0

    for count in phrase:
        if count_2 < count_1:
            phrase_is_reversed = word(phrase)+ space
            phrase = phrase_minus_first(phrase)
            count_2 += 1
            
    return phrase_is_reversed





#Question 2d

print("--------Problem 2d--------")
     
def main():
    phrase = input("Enter a phrase please: ")
    
    print("--------Problem 2a--------")
    problem_2a = word(phrase)
    print(problem_2a)
    
    print("--------Problem 2b--------")  
    problem_2b = phrase_minus_first(phrase)
    print(problem_2b)

    print("--------Problem 2c--------")  
    problem_2c = reversed_phrase(phrase)
    print(problem_2c)
main()


