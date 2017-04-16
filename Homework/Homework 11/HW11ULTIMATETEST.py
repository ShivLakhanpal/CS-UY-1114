'''def clean_data(complete_weather_filename, cleaned_weather_filename):
    
    weather_file = open(complete_weather_filename, "r")
    cleaned_weather_file = open(cleaned_weather_filename, "w")

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

def convert_data_to_metric(imperial_weather_filename, metric_weather_filename):
    imperial_file = open(imperial_weather_filename, "r")
    metric_file = open(metric_weather_filename, "w")

    metric_str = ""

    metric_str = metric_str + imperial_file.readline()

    for line in imperial_file:
        if line == "\n":
            metric_str = metric_str + "\n"

        else:
            stripped_line = line.strip()
            line_list = stripped_line.split(",")
            line_list[2] = f_to_c(line_list[2])
            line_list[3] = f_to_c(line_list[3])
            line_list[4] = in_to_cm(line_list[4])

            for index in range(4):
                metric_str = metric_str + line_list[index] + ","

            metric_str = metric_str + line_list[4] + "\n"

    metric_file.write(metric_str)

    metric_file.close()
    imperial_file.close()






'''weather_reader = csv.reader(weather_file)

    for line_str in weather_reader:
        print(line_str[0] + ',' + line_str[1] + ',' + line_str[2] \
              + ',' + line_str[3] + ',' + line_str[8], file = cleaned_weather_file)
    
    weather_file.close()
    cleaned_weather_file.close()'''
