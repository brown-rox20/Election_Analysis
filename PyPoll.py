# Add our dependencies.
import csv
import os
#Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis" , "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0
candidate_options = []
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # to do: perform analysis
    #Read the file oject with the reader function.
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    
    #Print each row in the CSV file.
    for row in file_reader:
        # Print the candidate name from each row.
        candidate_name = row[2]
        # 2. Add to the total vote count.
        total_votes += 1
        # if candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidate.
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
        

# 3. Print the candidate list.
print(candidate_votes)
        
# Use the with open statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write three counties to the file.
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
# Read the file object with the reader function.


# The data we need to retrieve.
# 1. the total number of votes cast
# 2. A complete list of candidates who received votes
# 3. A percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote