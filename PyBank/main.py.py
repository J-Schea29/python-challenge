#!/usr/bin/env python
# coding: utf-8

# In[29]:


#import needed modules
import os
import csv

#establishing path to file
csv_path = os.path.join(".", "Resources", "budget_data.csv")

#open csv file and set delimiter as ','
with open(csv_path) as csv_file:
    csvreader = csv.reader(csv_file, delimiter= ',')
    csv_header= next(csvreader)
    
    #declare variables
    total_profit = 0
    months = 0
    changes = []
    greatest_increase = [" ", 0]
    greatest_decrease = [" ", 99999999999999999]
    date_change = []
    
    
    First_csv = next(csvreader)
    previous = int(First_csv[1])
    months = int(months) + int(1)
    total_profit = int(total_profit) + int(First_csv[1])
    
    #loop through rows of the csv files performing actions
    for row in csvreader:
        
        #number of months
        months = int(months) + int(1)
        
        #calculate total profit/losses
        total_profit = int(total_profit) + int(row[1])
        
        Profit_Los.append(row[1])
        #subtracted the previous row from the current to get change
        change = int(row[1])- int(previous)
        #add to list 
        changes.append(change)
        date_change.append(row[0])
        #reset previous
        previous = row[1]
        
        if change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = change
        if change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = change
    
    #number of changes
    num_changes = len(changes)
    #find average change
    average_change = int(sum(changes))/int(num_changes)

   
    
    #print data found    
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${total_profit}")
    print(f"Average Change:{average_change}")
    print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
    print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

#imputing data in bank.analysis file

#establishing path to output file
outputpath = os.path.join(".","Analysis", "bank.analysis")

with open(outputpath, 'w') as csvfile: 
    
    csvwriter = csv.writer(csvfile, delimiter = ',')
    
    #title
    csvwriter.writerow(['Financial Analysis'])
    
    csvwriter.writerow(['------------------'])
    
    #The total number of months included in the dataset
    csvwriter.writerow([f"Total Months: {months}"])
    
    #The net total amount of “Profit/Losses” over the entire period
    csvwriter.writerow([f"Total: ${total_profit}"])
    
    #Calculate the changes in “Profit/Losses” over the entire period, then find the average of those changes
    csvwriter.writerow([f"Average Change:{average_change}"])
    
    #The greatest increase in profits (date and amount) over the entire period
    csvwriter.writerow([f"Greatest Increase in Profits:{greatest_increase[0]} (${greatest_increase[1]})"])
    
    #The greatest decrease in losses (date and amount) over the entire period
    csvwriter.writerow([f"Greatest Decrease in Profits:{greatest_decrease[0]} (${greatest_decrease[1]})"])


# In[ ]:




