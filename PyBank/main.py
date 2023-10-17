# import modules
import os
import csv
# source to read budget data file
fileload = os.path.join("Resources", "budget_data.csv")

# file to hold the output of the revenue analysis
outputfile = os.path.join("Analysis", "Financial Analysis.txt")

# variables
totalMonths = 0 # initialize the total months to 0
totalProfitLoss = 0
monthlyChanges = [] # empty list of monthly changes
months = [] # list of months

# read the csv file
with open(fileload) as budget_data:
    # create a csv reader object
    csvreader = csv.reader(budget_data)

    # read the header row
    header = next(csvreader)
    # move to the first row
    firstRow = next(csvreader)
   
   
    # increment the count of the total months
    totalMonths += 1
    
    # add on to the totla amount of revenue
        # profit is in index 1
    totalProfitLoss += float(firstRow[1])

    # establish previous profit/loss
        # revenue is in index 1
    previousProfitLoss = float(firstRow[1])

    for row in csvreader:
        # increment the count of the total months
        totalMonths += 1
        # add on to the totla amount of revenue
            # profit is in index 1
        totalProfitLoss += float(row[1])

        # calculate the net change 
        netChange = float(row[1]) - previousProfitLoss
        # add on to the list of monthly changes
        monthlyChanges.append(netChange)
        
        # add the first month that a change occured
            # month is in index 0
        months.append(row[0])

        # update the previous profit/loss
        previousProfitLoss = float(row[1])

# calculate the average net change per month
averageChangePerMonth = sum(monthlyChanges) / len(monthlyChanges)

greatestIncrease = [months[0], monthlyChanges[0]] # holds the month and valude of the greatest increase
greatestDecrease = [months[0], monthlyChanges[0]] # holds the month and valude of the greatest decrease

# use loop to calculate the index of the greatest and least monthly change
for m in range(len(monthlyChanges)):
    # calculate the greatest increase and greatest decrease
    if(monthlyChanges[m] > greatestIncrease[1]):
         # if the value is greater than the greatest increase, that value becomes the new greatest increase
         greatestIncrease[1] = monthlyChanges[m]
         # update the month
         greatestIncrease[0] = months[m]
    
    if(monthlyChanges[m] < greatestDecrease[1]):
         # if the value is less than the greatest decrease, that value becomes the new greatest decrease
         greatestDecrease[1] = monthlyChanges[m]
         # update the month
         greatestDecrease[0] = months[m]

# start generating the output
output = (
    f"Financial Analysis \n"
    f"------------------------------ \n"
    f"Total Months: {totalMonths} \n"
    f"Total: ${totalProfitLoss: ,.2f}\n"
    f"Average Change: ${averageChangePerMonth:,.2f}\n"
    f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]:,.2f}) \n"
    f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]:,.2f})"
    )
# print the output to console
print(output)    

# export the output to the txt file
with open(outputfile, "w") as textfile:
        textfile.write(output)