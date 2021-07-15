#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Poll Data

#import needed modules
import os
import csv

#establishing path to file
csv_path = os.path.join(".", "Resources 2", "election_data.csv")
#establishing path to output file
outputpath = os.path.join(".","Analysis", "poll.analysis")

#Declare Variables
candidate_list =[] 
candidate_votes = { }
candidate = [] 
total_votes = 0
Winner = " "
Winning_vote = 0

#open csv file and set delimiter as ','
with open(csv_path) as csv_file:
    csvreader = csv.reader(csv_file, delimiter= ',')
    csv_header= next(csvreader)
    
    
    for row in csvreader:
        total_votes = int(total_votes) +int(1)
        candidate = row[2] 
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidate_votes[candidate]= 0
            
        candidate_votes[candidate]= int(candidate_votes[candidate]) + int(1)
        
        
    print('Election Results')
    print('-------------------------------')
    print(f"Total Votes: {total_votes}")
    print('-------------------------------')
    
with open(outputpath, 'w') as txt_file: 
    
    #title
    txt_file.write('Election Results\n')
    txt_file.write('-------------------------------\n')
    
    #The total number of votes cast
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write('-------------------------------\n')
        
    for candidate in candidate_votes:
        vote = []
        votes = int(candidate_votes.get(candidate))
        vote_percentage = []
        vote_percentage = (float(votes)/float(total_votes) *100)
        if votes > Winning_vote:
            Winning_vote = votes
            Winner= candidate
           
        summary = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"   
        print(summary, end= "")
        
        txt_file.write(summary)
        
    print('-------------------------------')
    print(f"Winner: {Winner}")

    txt_file.write('-------------------------------\n')
    #The winner of the election based on popular vote
    txt_file.write(f"Winner: {Winner}")

