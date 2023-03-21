import datetime
import time
from playsound import playsound

# ask the user for how many minutes until the reminder
minutes = int(input("How many minutes until the reminder? "))

# calculate the reminder time
reminder_time = datetime.datetime.now() + datetime.timedelta(minutes=minutes)

# calculate the time difference
time_difference = reminder_time - datetime.datetime.now()

# convert the time difference to seconds
total_seconds = time_difference.total_seconds()

print("Meanwhile you can do your work , Don't Waste your Valuable Time")

# wait until the reminder time
time.sleep(total_seconds)

# play the sound file
playsound("buzzer.mp3")

# print the reminder message
print("It's time for your reminder!")
