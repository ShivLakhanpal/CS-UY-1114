import csv

weather_file = open('weather.csv', 'r')
cleaned_weather_file = open('yaya.csv', 'w')
weather_reader = csv.reader(weather_file)

heading = weather_file.readline()
space = ""
for line_str in weather_reader:
    for line in line_str:
        if line == "\n":
            print(line)
            print(line_str[0] + ',' + line_str[1] + ',' + line_str[2] \
                  + ',' + line_str[3] + ',' + line_str[8], file = cleaned_weather_file)
    
weather_file.close()
cleaned_weather_file.close()   

def clean_data(complete_weather_filename, cleaned_weather_filename):
    csv_file = open(complete_weather_filename, "r")
    clean_file = open(cleaned_weather_filename, "w")
    
    clean_str = ""
    
    for line in csv_file:
        if line == "\n":
            clean_str = clean_str + "\n"

        else:
            
            stripped_line = line.strip()
            line_list = stripped_line.split(",")
            required_data = []
            required_data.append(line_list[0])
            required_data.append(line_list[1])
            required_data.append(line_list[2])
            required_data.append(line_list[3])
            try:
                float(line_list[8])
                required_data.append(line_list[8])

            except ValueError:
                required_data.append('0')

            for index in range(4):
                clean_str = clean_str + required_data[index] + ","

            clean_str = clean_str + required_data[4] + "\n"

    clean_file.write(clean_str)

    clean_file.close()
    csv_file.close()'''
