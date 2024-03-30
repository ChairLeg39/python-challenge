# import csv module
import csv

# set path for file
csvpath_in = "PyBank/Resources/budget_data.csv"

# set variables
header = []
total_months = 0

# open csv file and read it
with open(csvpath_in, "r") as csvfile:
    # store contents of the csv file into csvreader
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # skip the header row, but store the header in header list
    header = next(csvreader)

    for row in csvreader:
        total_months += 1

print(total_months)


