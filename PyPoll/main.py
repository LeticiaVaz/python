import csv
import os




with open ('election_data.csv') as file:
    reader = csv.DictReader(file, delimiter=',')

    candidates = []
    num_votes = []
    total_votes=0
    votes_percentage= []
    for rows in reader:
        total_votes +=1
        if rows['Candidate'] not in candidates:

            candidates.append(rows['Candidate'])
            index = candidates.index(rows['Candidate'])
            num_votes.append(1)
        else:
            index=candidates.index(rows['Candidate'])
            num_votes[index]+=1
     
    for votes in num_votes:
        percent = (votes/total_votes)*100
        percent = "%.3f%%" % percent
        votes_percentage.append(percent)

    #Find the winning candidate
    winner = max(num_votes)
    index=num_votes.index(winner)
    winning_candidate=candidates[index]


print('  Election Results')
print('------------------------')
print(f"Total Votes: {str(total_votes)}")
print ('---------------------------')
for summary in range(len(candidates)):
    summary = (f"{candidates[summary]}: {str(votes_percentage[summary])} ({str(num_votes[summary])}")
    print(summary)

print ('---------------------------')
print ('Winner: ',winning_candidate)
