'''

Shiv Lakhanpal
CS 1114
svl238

To print out a CSV file that creates different files
'''

import csv
# Part A
def clean_data(complete_weather_filename, cleaned_weather_filename):
    

    weather_file = open('weather.csv', 'r')
    cleaned_weather_file = open('yaya.csv', 'w')
    weather_reader = csv.reader(weather_file)

    for line_str in weather_reader:
        print(line_str[0] + ',' + line_str[1] + ',' + line_str[2] \
              + ',' + line_str[3] + ',' + line_str[8], file = cleaned_weather_file)
    
    weather_file.close()
    cleaned_weather_file.close()    


# Part B
def f_to_c(f_temperature):
    return ((f_temperature - 32) * (5/9))


def in_to_cm(inches):
    return (inches * 2.54) # modify this

def convert_data_to_metric(imperial_weather_filename, metric_weather_filename):
    
    csv_imperial_file = open(imperial_weather_filename, "r")
    csv_metric_file = open(metric_weather_filename, "w")
    
    space = ''
    comma = ','
    metric_file = space
    metric_file += imperial_file.readline()

    for row in csv_imperial_file:
        
        if row == '\n':
            
            metric_file += '\n'

        else:
            
            line_s = line.strip()
            list_csv = line_s.split(",")
            list_csv[2] = f_to_c(list_csv[2])
            list_csv[3] = f_to_c(list_csv[3])
            list_csv[4] = in_to_cm(list_csv[4])

            for index in range(4):
                
                metric_str  += list_csv[index] + comma

            metric_file += list_csv[4] + '\n'

    metric_file.write(metric_file)
    
    csv.imperial_file.close()
    csv.metric_file.close()

    
    
    # Similar to clean_data() - read in the file and make a new file with metric values.


# Part C
def print_averages_per_month(city, weather_filename, unit_type):
    # prints average highs and lows in each month for the given city


# Part D
# Write your question (as a comment), and implement a function to answer it



def main():
    print ("Running Part A")
    clean_data("weather.csv", "weather in imperial.csv")
    
    print ("Running Part B")
    convert_data_to_metric("weather in imperial.csv", "weather in metric.csv")
    
    print ("Running Part C")
    print_average_temps_per_month("San Francisco", "weather in imperial.csv", "imperial")
    print_average_temps_per_month("New York", "weather in metric.csv", "metric")
    print_average_temps_per_month("San Jose", "weather in imperial.csv", "imperial")

    print ("Running Part D")
    # add your code here
    

    
main()

