import csv

with open('./logs/internetspeed.csv') as f:
    reader = csv.reader(f)
    loglist = list(reader)
    print(loglist)

#average download
counter = 0
total = 0
for i in range(len(loglist)):
    total += int(loglist[i][3])
    counter += 1

print("Total measurements: " + str(counter))
print("Average download: " + str(round(total/counter)))

slow = 0
fast = 0
threshold = 15
for i in range(len(loglist)):
    ds = int(loglist[i][3])
    if ds < threshold:
        slow += 1
    else:
        fast += 1
downtime = slow/(slow + fast)*100
print("Downtime is: " + str(downtime))