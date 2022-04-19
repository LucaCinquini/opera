from datetime import datetime
from datetime import timedelta
import time

date_format_str = "%Y-%m-%d %H:%M:%S"
start_datetime_str = "2020-01-01 00:00:00"
time_increment_minutes = 600
number_of_iterations = 24*7

# change this to 3600 seconds to run every hour
wait_time_seconds = 0

start_datetime = datetime.strptime(start_datetime_str, date_format_str)
for i in range(0, number_of_iterations):
  start = start_datetime + timedelta(minutes=i*time_increment_minutes)
  stop = start_datetime + timedelta(minutes=(i+1)*time_increment_minutes)
  print(f"{start} --> {stop}")
  time.sleep(wait_time_seconds)
