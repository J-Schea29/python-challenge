# python-challenge

# Part 1
For this challenge, I had to anlyse finacial records for a company. These records are contained in budget_data.csv.
```python
#establishing path to file
csv_path = os.path.join(".", "Resources", "budget_data.csv")
#open csv file and set delimiter as ','
with open(csv_path) as csv_file:
    csvreader = csv.reader(csv_file, delimiter= ',')
    csv_header= next(csvreader)
```
Using this csv I had to find the total number of months included in the dataset, net total amount of “Profit/Losses” over the entire period, the changes in “Profit/Losses” over the entire period, the averagechange in “Profit/Losses” over the entire period, greatest increase in profits (date and amount) over the entire period, and greatest decrease in losses (date and amount) over the entire period. The results were: 
```python
Financial Analysis

------------------

Total Months: 86

Total: $38382578

Average Change:-2315.1176470588234

Greatest Increase in Profits:Feb-2012 ($1926159)

Greatest Decrease in Profits:Sep-2013 ($-2196167)
```

 This an assignment for UC Davis' Data Anlytics Program. This project had two parts. For the first, I used python to analyze finacial data, export my final summary of the data to another file. Second, I analysed polling data with python and exported this as well to another file. 
