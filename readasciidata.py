# In this assignment you will analyse the meteorological data contained in a file on the student portal called Basel_weather_2016_daily_simple.csv.
# .csv is the file extension for a table of comma-separated values.

# MARK SCHEME:
# 0/5 - Very limited or no attempt for any sections.
# 1/5 - Limited attempt at some questions but none/very little working/correct sections. Comments and code quality very limited.
# 2/5 - Some attempt at all sections, but none or few working/correct. Comments and code quality limited.
# 3/5 - Mostly working/correct solutions to all mandatory sections. Comments and code quality satisfactory.
# 4/5 - Substantially correct solutions to all mandatory sections. Comments and code quality good.
# 5/5 - Entirely working/correct solutions to all mandatory sections. Comments and code quality excellent.

# Pay attention to how the data is read and formatted because you will be writing similar scripts later in the course.

# a module for plotting
import matplotlib.pyplot as plt

# data file name (file should be in the same directory as this script)
filename = 'Basel_weather_2016_daily_simple.csv'

# read in the data from given file.
# datafile is an object of type file.
# ASCII (American Standard Code for Information Interchange) is a standard data format for storing plain text (without formatting).
# TODO: open the file for reading, specify ASCII encoding.
datafile = open(...)

print('reading data from', filename)

# read the first line
columns = datafile.readline()
# split columns string into semicolon-separated values
columns = columns.split(';')
print('\n column labels: \n', columns)

# daily mean temperatures - initialise as empty list
temps = []

# loop over all rows in datafile
for row in datafile:
    # TODO: split the row string, loop through the results, and convert each value to a floating-point number, saving as a list
    # Hints: use string.split use https://docs.python.org/3.7/library/stdtypes.html#str.split
    # See the examples here to convert to a floating-point number: https://docs.python.org/3.7/library/functions.html?highlight=float#float

    # TODO: add the temperature to the end of the list using append
    # Hint: Its the 6th column, and they are zero-indexed.

# list now contains daily mean temperature values
print('\n daily mean temperature: \n', temps)


# MANDATORY QUESTIONS (ATTEMPT ALL):

# download the ASCII file Basel_weather_2016_daily_simple.csv from the student portal.

# 1. Complete the lines marked 'TODO:' to complete the script - ensure it runs, and check the output temperatures against the source data.

# 2. Plot daily mean temperature using matplotlib.pyplot
#    Use plt.show() to see the figure.
#    Write code to save the plot with a suitable file name and extension (i.e. do not just use the save button in the figure popup window).

# 3. In the same figure, plot daily max and min temperature (hint: what columns are max and min temperature?)
#    Add axis labels, legend and title, and make the plot presentable with nice colours and large font size.
#    You will need to consult the Python help or search online for how to do this.
#    You should use the labels stored in the 'columns' variable to create the legend entries rather than manually writing them.

# 4. Get the daily mean wind speed in m/s (the data file contains wind speed in km/h).
#    Create a new figure, plot daily mean wind speed (m/s) and save it with a suitable file name and extension.

# 5. Compute the total annual precipitation, maximum and minimum annual temperatures and print them.


# OPTIONAL EXTENSION QUESTIONS (UNCREDITED) - if you have completed all the tasks above:
# 5. Use the 'with' statement to safely close the file. Why is this advantageous?
# 6. Use a list comprehension instead of a loop for looping through the values in the different columns (line ~40).

# Upload your script to the student portal under Assignment 1.
# Please include your surname at the start of the filename e.g. BlameyBen_Assignment1.py
# It should be possible to run the script to produce all of the figures and annual values without us having to modify it in any way.
# Make sure your script is suitably commented.


# Created 2017 by jonathan.bull@it.uu.se and louis.j.van.rensburg@gmail.com
# Revised 2018 Ben Blamey ben.blamey@it.uu.se