print("The current population of the United States is 307357870")

years = int(input("Enter a number to see the population of the United States of any year: "))


min_in_hour = 60
seconds_in_min = 60
hours_in_a_day = 24
days_in_a_year = 365

seconds_in_a_year = seconds_in_min*min_in_hour*hours_in_a_day*days_in_a_year

birth = seconds_in_a_year // 7 
death = seconds_in_a_year // 13
immigrant = seconds_in_a_year //35

Totalpop = 307357870 + years*birth + years*immigrant - years*death

print("The estimated population in",years,"years is",Totalpop)

