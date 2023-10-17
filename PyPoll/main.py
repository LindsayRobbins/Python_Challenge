import os
import csv

# setting the file path for my election data csv file
inputFile = os.path.join("Resources", "election_data.csv")

outputfile = os.path.join("Analysis", "Election_Results.txt")

totalVotes = 0 # variable that holds the number of votes
candidateList = [] # list that holds the candidates in the data
candidateVotes ={} # dicitonary that will hold the votes per candidate
winningCount = 0 # variable hold the winning count
winningCandidate = "" # variable to hold the winning candidate

with open(inputFile, "r") as csvFile:
    # creating the reader object
    csvReader = csv.reader(csvFile, delimiter=",")
    # reading the headers
    csvheader = next(csvReader)

    # rows will be lists
        # index 0 is the ballot ID
        # index 1 is the county
        # index 3 is the candidate
    
    # for each row
    for row in csvReader:
        # add on to the total votes
        totalVotes += 1

        # check to see if the candidate is in the list of candidates
        if row[2] not in candidateList:
            # if the candidate is not in the list add the candidate to the list
            candidateList.append(row[2])

            # add the value to the dictionary
            # { "key": value}
            # astart teh count at 1 for the votes
            candidateVotes[row[2]] = 1
        
        else: 
            # the candidate is in the list of candidates
            # add a vote to that candidate
            candidateVotes[row[2]] += 1


voteOutput = ""
for candidate in candidateVotes:
    # get the vote count and the percentage of the votes
    votes = candidateVotes.get(candidate)
    votePct = (float(votes) / float(totalVotes)) * 100.00
    
    voteOutput += f"{candidate}: {votePct:.3f}% ({votes}) \n"
    
    
    if votes > winningCount:
        winningCount = votes
        # update the winning candidate
        winningCandidate = candidate

winningCandidateOutput = f"Winner: {winningCandidate}\n--------------------------"

# create an output variable to hold the output
output = (
    f"Election Results\n"
    f"--------------------------\n"
    f"Total Votes: {totalVotes}\n"
    f"--------------------------\n"
    f"{voteOutput}\n"
    f"--------------------------\n"
    f"{winningCandidateOutput}"
)
# print the output to the terminal
print(output)

# print the results and export the data to a text file
with open(outputfile, "w") as textFile:
# write the output to the text file
    textFile.write(output)
