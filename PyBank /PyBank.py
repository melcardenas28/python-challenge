import os
import csv

csvpath = os.path.join("Resources", "/Users/melissa/Downloads/Python Homework /PyBank /Resource /budget_data.csv")
Output_text = os.path.join("Analysis", "/Users/melissa/Downloads/Python Homework /PyBank /Analysis/budget_analysis.txt")

with open(csvpath) as csvfile:

# List and Variables 
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader) 
    revenue = []
    date = []
    change = []

    for row in csvreader:
        revenue.append(float(row[1]))
        date.append(row[0])

    for i in range(1,len(revenue)):
        change.append(revenue[i] - revenue[i-1])   
        avg_change = round(sum(change)/len(change),2)
        max_change = round(max(change))
        min_change = round(min(change))
        max_change_date = str(date[change.index(max(change))])
        min_change_date = str(date[change.index(min(change))])

Output = (
"Financial Analysis\n"
"----------------------------\n"
f"Total Months: {len(date)}\n"
f"Total: ${round(sum(revenue))}\n"
f"Average Change: ${avg_change}\n"
f"Greatest Increase in Profits: {max_change_date} (${max_change})\n"
f"Greatest Decrease in Profits: {min_change_date} (${min_change})\n"  
)
print(Output, end="")

# Create Analysis Folder with a text file
txt_file = open(Output_text, "w")
txt_file.write(Output)
txt_file.close()