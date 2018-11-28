"""Script designed to read meteorological data in CSV file and plot it appropriately """
# Modules for plotting and reading csv files
import matplotlib.pyplot as plt
import csv

# data file name (file should be in the same directory as this script)
filename = 'Basel_weather_2016_daily_simple.csv'

# several lists initialised as empty
mean_temps = []
max_temps = []
min_temps = []
total_precip = []
wind_speed = []

# 1. used csv method to open file and separate values using the ';' delimiter
# specifying ASCII is unnecessary as it is already the default for the method.
with open(filename, 'r') as datafile:
    reader = csv.reader(datafile, delimiter=';')
    line_count = 0
    for row in reader:
        if line_count == 0:
            columns = row
            #print('\n Column labels: \n', columns)
            line_count += 1
        else:
            data_list = [float(i) for i in row]                       # converts items into floats
            #print(f'\n Row {line_count}\n', data_list)
            mean_temps.append(data_list[5])                           # appends items to new list will be used later
            max_temps.append(data_list[14])                           # for plotting and calculations.
            min_temps.append(data_list[15])
            total_precip.append(data_list[8])
            wind_speed.append(data_list[12])
            line_count += 1

# 2. plot daily mean temp
plt.plot(mean_temps, label=columns[5], color='green')
# 3. plot min and max temp
plt.plot(max_temps, label=columns[14], color='red')
plt.plot(min_temps, label=columns[15], color='blue')
plt.xlabel('Day of the year', fontsize=18)
plt.ylabel('Temperature (°C)', fontsize=18)
plt.title('Temperatures of 2016', fontsize=22)
plt.legend()
plt.savefig('Daily mean temp.png')                                  # saves image as .png
plt.show()

# 4. daily mean wind speed calc and plot
ms_wind = [round(item / 3.6, 2) for item in wind_speed]             # converts values from km/h to m/s
plt.plot(ms_wind, label=columns[12], color='orange')
plt.xlabel('Day of the year', fontsize=18)
plt.ylabel('Wind speed (m/s)', fontsize=18)
plt.title('Annual wind speed', fontsize=22)
plt.legend()
plt.savefig('Annual wind speed.png')                                # saves image as .png
plt.show()

# 5. computing total annual precipitation
print('Total annual precipitation: '+ str(sum(total_precip)))
print('Maximum annual temperature: ' + str(max(max_temps))+' °C')
print('Minimum annual temperature: ' + str(min(min_temps))+' °C')