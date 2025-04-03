FROM python:3.8-buster
RUN apt-get update && apt-get install -y cron busybox nano && pip install speedtest-cli && pip install pytz
COPY speedtestlogger.py /app/speedtestlogger.py
COPY logs/internetspeed.csv /logs/internetspeed.csv
COPY crontab /tmp/root.crontab
RUN crontab /tmp/root.crontab && chmod +x /app/speedtestlogger.py && service cron reload
CMD mkdir /logs2; printenv >> /etc/environment; printenv >> /etc/default/locale; busybox syslogd -C; cron -L 2 -f; service cron reload