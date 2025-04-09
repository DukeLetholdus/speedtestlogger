import csv

with open('./logs/internetspeed.csv') as f:
    reader = csv.reader(f)
    loglist = list(reader)

# average download
counter = 0
total = 0
for i in range(len(loglist)):
    total += int(loglist[i][3])
    counter += 1

with open("./logs/output.txt", "w") as text_file:
    print("Total measurements: {counter}".format(counter=counter), file=text_file)
    print("Average download: {average} mbps".format(average=round(total/counter, 1)), file=text_file)

# calculate percentage internet bad
slow = 0
fast = 0
threshold = 15
for i in range(len(loglist)):
    ds = int(loglist[i][3])
    if ds < threshold:
        slow += 1
    else:
        fast += 1
downtime = round(slow/(slow + fast)*150, 1)
with open("./logs/output.txt", "a") as text_file:
    print("Downtime is: {downtime}%".format(downtime=downtime), file=text_file)