import json 

#Read the file
with open("precipitation.json", "r") as file:
    rain= json.load(file)
#print(rain)

#Create empty list
seattle= [0]*12

#Only include Seattle
for entry in rain:
    if entry["station"] == "GHCND:US1WAKG0038":
        # Filter the month out of date string and convert into integer
        month = int(entry["date"].split('-')[1])
        # Rainfall value
        rainfall = (entry["value"])
        # This code indexes each element with the month and then tallies the total rainfall for each month
        seattle[month-1] += rainfall

print(seattle)

#Total rainfall
print(sum(seattle)) 

total_rain= sum(seattle)

#Relative percipitation per month
average= []
for element in seattle:
    average.append(element/total_rain)
print(average)






