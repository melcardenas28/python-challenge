import os
import csv
# Load Files 
csvpath = os.path.join("Resources", "/Users/melissa/Downloads/Python Homework /PyPoll/Resources/election_data.csv")
output_text = os.path.join("Analysis", "/Users/melissa/Downloads/Python Homework /PyPoll/Analysis/election_analysis.txt")

# lists and Variables
total_votes = 0
candidates_unique = []
candidate_votes = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        total_votes += 1
        candidate_in = (row[2])
        if candidate_in in candidates_unique:
            candidate_index = candidates_unique.index(candidate_in)
            candidate_votes[candidate_index] = candidate_votes[candidate_index] + 1
        else:
            candidates_unique.append(candidate_in)
            candidate_votes.append(1)

percentage = []
max_votes = candidate_votes[0]
max_index = 0

for x in range(len(candidates_unique)):
    vote_percentage = round(candidate_votes[x]/total_votes*100, 2)
    percentage.append(vote_percentage)
    if candidate_votes[x] > max_votes:
        max_votes = candidate_votes[x]
        max_index = x
election_winner = candidates_unique[max_index] 

# Generate Output Summary
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')
for x in range(len(candidates_unique)):
    print(f'{candidates_unique[x]} : {percentage[x]:.3f}% ({candidate_votes[x]})')
print('-------------------------')
print(f'Winner: {election_winner}')
print('-------------------------')

# Export the results to text file
with open(output_text, "w", newline="") as txt_file:
    txt_file.write('Election Results\n')
    txt_file.write('-------------------------\n')
    txt_file.write(f'Total Votes: {total_votes}\n')
    txt_file.write('-------------------------\n')
    for x in range(len(candidates_unique)):
        txt_file.write(f'{candidates_unique[x]} : {percentage[x]:.3f}% ({candidate_votes[x]})\n')
    txt_file.write('-------------------------\n')
    txt_file.write(f'Winner: {election_winner}\n')
    txt_file.write('-------------------------\n')
