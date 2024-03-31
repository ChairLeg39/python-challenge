#  import csv module
import csv

# Needed:
# 1. The total number of votes cast - done
# 2. A complete list of candidates who received votes - done*
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# set path for file
election_file_path = "PyPoll/Resources/election_data.csv"

# set variables
total_votes = 0
candidates = []
header = []
candidates_votes = {} # key is candidate name, value is vote count
votes = 0
max_votes = 0
winner = str()

# open csv file and read it 
with open(election_file_path, 'r') as election_file:
    
    # store contents of the csv file into csv_file
    csv_file = csv.reader(election_file)

    # skips the header row, stores column headers in header
    header = next(csv_file)
    # print(header[0])
    # print(header[1])
    # print(header[2])

    # read a row in the file, loop through each row
    for row in csv_file:
        
        # add to total votes
        # counts the number of rows to sum up total votes
        total_votes += 1

        # "Ballot ID,County,Candidate"
        ballot_id = row[0]
        county = row[1]
        candidate = row[2]
        
        # check to see if the candidate exists
        if candidate not in candidates:
            # add to list if they haven't been added to the list
            candidates.append(candidate)

        # check to see if the candidate exists in the dictionary (same as comic book)
        if candidate not in candidates_votes:
            candidates_votes[candidate] = 1
        else:
            # sum up votes for each candidate
            candidates_votes[candidate] += 1

# search for candidate in the candidate_votes dict
for candidate in candidates_votes.keys():
    
    # store vote count for each candidate as int
    votes = candidates_votes[candidate]
    # print(candidate) prints candidate names
    # print(votes) prints the votes count as int
    # print(candidates_votes) prints the whole dict as key value pairs
    
    # calc winner based on popular vote
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# print(winner)
# print(max_votes)

out_file_path = "PyPoll/Analysis/election_data_analysis.txt"

with open(out_file_path, 'w') as analysis:
    analysis.write('Election Results\n'
                    '-----------------------------------\n'
                    f'Total Votes: {total_votes}\n'
                    '-----------------------------------\n'
                    f'\n'
                    f'\n'
                    f'\n'
                    '-----------------------------------\n'
                    f'Winner: {winner}')


# print the results to screen
# print('Election Results')
# print('-------------------------')
# print(f'Total Votes: {total_votes}')
# print('-------------------------')

# print(len(candidates), "candidates")
# print(candidates[0])
# print(candidates[1])
# print(candidates[2])
# print(candidates, "candidates")
# print the results to file


# end here

# example output
# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------