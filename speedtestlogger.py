import speedtest
import csv
import datetime
import time
import pytz
import os

def test_internet_speed():
    down = 0
    up = 0
    wait = 120
    try:
        st = speedtest.Speedtest(secure=1)
        down += round(st.download() / 1000000)  # Perform the download speed test and convert to Mbps
        up += round(st.upload() / 1000000)  # Perform the upload speed test and convert to Mbps
    except speedtest.SpeedtestException as e:
        time.sleep(wait)
        try:
            st = speedtest.Speedtest(secure=1)
            down += round(st.download() / 1000000)  # Perform the download speed test and convert to Mbps
            up += round(st.upload() / 1000000)  # Perform the upload speed test and convert to Mbps
        except:
             down = up = 0
    return down, up

# Set variables
print("started")
tz = os.environ['TZ']
print(tz)
down, up = test_internet_speed()
print("speedtest succeeded")
dt = datetime.datetime.now(pytz.timezone(tz)).date().strftime("%Y-%m-%d")
tm = datetime.datetime.now(pytz.timezone(tz)).time().strftime("%H:%M:%S")
dttm = datetime.datetime.now(pytz.timezone(tz)).strftime("%Y/%m/%d %H:%M:%S")
print("dates gathered")
toappend = [dttm, dt, tm, down, up]
# Write to CSV if test succeeded
if down > 0 and up > 0:
    with open('/logs/internetspeed.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(toappend)
print("writing succeeded")