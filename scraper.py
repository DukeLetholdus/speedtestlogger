import csv
import datetime

with open('./logs/internetspeed.csv') as f:
    reader = csv.reader(f)
    loglist = list(reader)

# Declare hot times (time1-time2, time3-time4)
time1 = datetime.time(6,30)
time2 = datetime.time(9)
time3 = datetime.time(17,30)
time4 = datetime.time(22,30)

# average download
counter = 0
total = 0
for i in range(len(loglist)):
    total += int(loglist[i][3])
    counter += 1
with open("./logs/output.txt", "w") as text_file:
    print("Total measurements: {counter}".format(counter=counter), file=text_file)
    print("Average download: {average} mbps".format(average=round(total/counter, 1)), file=text_file)

# average download low hours
counter = 0
total = 0
for i in range(len(loglist)):
    mtime = datetime.datetime.strptime(loglist[i][2], '%H:%M:%S').time()
    ds = int(loglist[i][3])
    if (mtime > time4 and mtime < time1) or (mtime > time2 and mtime < time3):
        total += int(loglist[i][3])
        counter += 1
with open("./logs/output.txt", "a") as text_file:
    print("Average download low hours: {average} mbps".format(average=round(total/counter, 1)), file=text_file)

# average download hot hours
counter = 0
total = 0
for i in range(len(loglist)):
    mtime = datetime.datetime.strptime(loglist[i][2], '%H:%M:%S').time()
    ds = int(loglist[i][3])
    if (mtime > time1 and mtime < time2) or (mtime > time3 and mtime < time4):
        total += int(loglist[i][3])
        counter += 1
with open("./logs/output.txt", "a") as text_file:
    print("Average download hot hours: {average} mbps".format(average=round(total/counter, 1)), file=text_file)

# calculate percentage internet bad
slow = 0
fast = 0
threshold = 15
for i in range(len(loglist)):
    ds = int(loglist[i][3])
    if ds < threshold: slow += 1
    else: fast += 1
downtime = round(slow/(slow + fast)*100, 1)
with open("./logs/output.txt", "a") as text_file:
    print("Downtime is: {downtime}%".format(downtime=downtime), file=text_file)

# calculate quality in hot hours
slow = 0
fast = 0
threshold = 15
for i in range(len(loglist)):
    mtime = datetime.datetime.strptime(loglist[i][2], '%H:%M:%S').time()
    ds = int(loglist[i][3])
    if (mtime > time1 and mtime < time2) or (mtime > time3 and mtime < time4):
        if ds < threshold: slow += 1
        else: fast += 1
downtime = round(slow/(slow + fast)*100, 1)
with open("./logs/output.txt", "a") as text_file:
    print("Downtime in hot hours is: {downtime}%".format(downtime=downtime), file=text_file)
    print("slow: {slow} times".format(slow=slow), file=text_file)
    print("fast: {fast} times".format(fast=fast), file=text_file)
