#A bug collector collects bugs everyday for seven days. Write a program that keeps a running total of the number of bugs collected during the seven days.

#Set total = 0
# for each of 7 days: 
#Import bugs collected for a day
#Add bugs collected to toal 


total = 0

# Get the bugs collected for each day.

for day in range(1, 8) :
    print('Enter the number of bugs collected on day', day)
    bugs = int(input())
    total += bugs


# Print the total number of bugs collected.

print('Total number of bugs collected in seven days is', total)
