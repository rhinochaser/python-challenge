
# main.py for PyBank

# Your task is to create a Python script that analyzes the records to calculate each of the following:
# The total number of months included in the dataset
# The total amount of revenue gained over the entire period
# The average change in revenue between months over the entire period
# The greatest increase in revenue (date and amount) over the entire period
# The greatest decrease in revenue (date and amount) over the entire period

# Financial Analysis
#----------------------------
# Total Months: 25
# Total Revenue: $1241412
# Average Revenue Change: $216825
# Greatest Increase in Revenue: Sep-16 ($815531)
# Greatest Decrease in Revenue: Aug-12 ($-652794)

# Dependencies
import os
import csv

#make a prompt for the user to choose a file 1 or 2 and assign it to a var named file
user_file_choice = input("pick a budget document to run 1 or 2: ")
if int(user_file_choice) == 1:
    # pathway to budget doc
    file = os.path.join("budget_data_1.csv")
    print ('file 1 will process \'budget_data_1.csv\'')
elif int(user_file_choice) == 2:
    # pathway to budget doc
    file = os.path.join("budget_data_2.csv")
    print ('file 2 will process \'budget_data_2.csv\'')
else:
    print ("you did not choose a valid choice, please try again")

# Analysis variables:
total_months = 0.0
total_revenue = 0
avg_rev_change = 0.0
greatest_increase = 0.0
greatest_decrease = 0.0
current_month_rev = 0.0
last_month_rev = 0.0

# tracker list of revenue changes:
change_in_rev = []
month_change_in_rev = []


# open and read the CSV files
with open(file, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip the header row
    next(csvreader)

    # loopp through budget data with a for loop:
    for rows in csvreader:

        #Calulate total months in the data:
        total_months = total_months + 1

        #Calculate total_revenue:
        current_month_rev = float(rows[1])
        total_revenue = total_revenue + current_month_rev

        # populate the rev storage list trackers:
        if total_months > 1:
            change = current_month_rev - last_month_rev
            change_in_rev.append(change)
            month_change_in_rev.append(rows[0])

        last_month_rev = current_month_rev

    # calculate the average revenue change via looping through rev storage lists
    total_change = 0.0

    for i in range(len(change_in_rev)):
        total_change = total_change + change_in_rev[i]

        if change_in_rev[i] > 0 and change_in_rev[i] > greatest_increase:
        greatest_increase = change_in_rev[i]
        greatest_month_increase = month_change_in_rev[i]
        if change_in_rev[i] < 0 and change_in_rev[i] < greatest_decrease:
            greatest_decrease = change_in_rev[i]
            greatest_month_decrease = month_change_in_rev[i]

    avg_rev_change = total_change / len(change_in_rev)


    print("\n\n")

    print("Financial Analysis of " + file)
    print("---------------------------------------------")

    print("Total Months: " + str(total_months))
    print("Total Revenue: $" + str(total_revenue))

    print("Average Revenue Change: $" + str(round(avg_rev_change, 2)))

    print("Greatest Increase in Revenue: " + greatest_month_increase + " ($" + str(greatest_increase) + ")")

    print("Greatest Decerease in Revenue: " + greatest_month_decrease + " $" + str(greatest_decrease) + ")\n\n")

# write to output file:

output_file = os.path.join('Analyzed ' + str(file) + ".txt")

with open(output_file, 'w') as txtfile:

    txtfile.write("Financial Analysis\n")
    txtfile.write("---------------------------------------------\n\n")
    txtfile.write("Total Months: " + str(total_months) + "\n")
    txtfile.write("Total Revenue: $" + str(total_revenue) + "\n")

    txtfile.write("Average Revenue Change: $" + str(round(avg_rev_change, 2))+ "\n")

    txtfile.write("Greatest Increase in Revenue: " + greatest_month_increase + " ($" + str(greatest_increase) + ")\n")

    txtfile.write("Greatest Decerease in Revenue: " + greatest_month_decrease + " $" + str(greatest_decrease) + ")\n\n")






