
import csv
import os
print ("Financial Analysis")
print('-----------------------')

csvpath = os.path.join("..","Resources","budget_data.csv")

with open(csvpath, newline="" ) as file:

    reader = csv.DictReader(file, delimiter=',')

# The total number of months included in the dataset  
    print('Total months: ',len({row['Date'] for row in reader}))


# The total number of months included in the dataset 

rows = []
with open(csvpath,newline="") as file:
    
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        rows.append(int(row['Profit/Losses']))
    
print ('Total: ',sum(rows))
  

# The average of the changes in "Profit/Losses" over the entire period

with open(csvpath,newline="") as f:
    lines = f.readlines()

data = []

for line in lines[1:]: #don't read the first line containing month and amount
    line = line.strip("\n") #erase the newline character from each line
    data.append(line.split(",")) #split the lines using the comma as a delimiter

output = []
for index,element in enumerate(data[1:]): #we start in the second element because we will subtract the first one
    output.append(int(element[1])-int(data[index][1]))

average = sum(output)/len(output)


print ('Average Change: ',round(average,2))


#print (output)
print ((index.(,max(output))) , '(',max(output),')')


# The greatest decrease in losses (date and amount) over the entire period

print ((output.index(min(output))) , '(',min(output),')')

# As an example, your analysis should look similar to the one below:

