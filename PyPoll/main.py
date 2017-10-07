# main.py for PyPoll

import os
import csv

# Variables
total_votes = 0
candidates = {} # {candidate name: number of votes}
percent_of_votes = 0.0

# file pathway
electionCSV = os.path.join("election_data_2.csv")

# open and read the CSV file
with open(electionCSV, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip header row
    next(csvreader, None)

    # Loop through election data
    for rows in csvreader:
        # total number of votes
        total_votes = total_votes + 1

        candidate = rows[2]

        #if existing candidate, add to his/her total votes; otherwise add to candidates dictionary, 1 vote
        if candidate in candidates:
            candidates[candidate] = candidates[candidate] + 1

        else:  #add this candidate with 1 vote
            candidates[candidate] = 1

    # write to output text file

    output_file = os.path.join('Poll_Results_' + 'election_data_2' +'.txt')
    with open(output_file, 'w') as txtfile:


        #print to screen
        print("Election Results")
        print("----------------------------------------")
        print("Total Votes: " + str(total_votes))
        print("----------------------------------------")

        #print to file
        txtfile.write("Election Results\n")
        txtfile.write("---------------------------------------------\n")
        txtfile.write("Total Votes: " + str(total_votes) + "\n")
        txtfile.write("---------------------------------------------\n")

        winner = ""
        winner_votes = 0
        #loop through candidate dict; print out percent and total votes
        for i in candidates:
            #compute percentage
            candidate_votes = candidates[i]
            percent_of_votes = round(100.0 * candidate_votes/total_votes,2)

            #print and write candidate vote total
            print(i + ":\t" + str(percent_of_votes) + "% (" + str(candidate_votes) + ")")
            txtfile.write(i + ":\t" + str(percent_of_votes) + "% (" + str(candidate_votes) + ")\n")

            #winner
            if candidate_votes > winner_votes:
                winner_votes = candidate_votes
                winner = i

        print("----------------------------------------")
        print ("Winner: " + winner)
        print("----------------------------------------")

        txtfile.write("---------------------------------------------\n")
        txtfile.write("Winner: " + winner + "\n")
        txtfile.write("---------------------------------------------\n")





