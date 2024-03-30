# import csv module
import csv

# set path for file
csvpath_in = "PyBank/Resources/budget_data.csv"

# set variables
header = []
total_months = 0

# open csv file and read it
with open(csvpath_in, 'r') as csvfile:
    # store contents of the csv file into csvreader
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # skip the header row, but store the header in header list
    header = next(csvreader)

    for row in csvreader:
        total_months += 1



out_file_path = "PyBank/Analysis/budget_data_analysis.txt"

with open(out_file_path, 'w') as analysis:
    analysis.write('Financial Analysis\n'
                    '-----------------------------------\n'
                    f'Total Months: {total_months}\n'
                    f'Total: \n'
                    f'Average Change: \n'
                    f'Greatest Increase in Profits: \n'
                    f'Greatest Decrease in Profits: \n')
