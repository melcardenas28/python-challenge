#after finishing the command lines follow the video to update git hub

#Modules
import os
import csv

# Set path for file
csvpath = os.path.join("..", "Resources", "02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

# Lists to store data
total_months = []
total_profit = []
average_change = []

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip the headers
    header = next(csvreader)  
    print(header)

    for row in csvreader:
        # Add total months and total 
        total_months.append(row[0])
        total_profit.append(int(row[1]))

# run through profits to calculate the total change
    for i in range(len(total_profit)-1):
        
        # we are taking the difference between the months and appending them
        average_change.append(total_profit[i+1]-total_profit[i])
        
# min and max of profits 
max_increase_value = max(average_change)
max_decrease_value = min(average_change)

# with consideration of the next month (+1) calculate the increase and cosider months 
max_increase_month = average_change.index(max(average_change)) + 1
max_decrease_month = average_change.index(min(average_change)) + 1

# print statements
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(average_change)/len(average_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
# not sure how to do the print statements 