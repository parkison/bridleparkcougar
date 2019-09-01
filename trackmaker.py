import datetime
import random

start_time = datetime.datetime.strptime('Jul 26 2019  3:23PM', '%b %d %Y %I:%M%p')
duration_minutes = 58
duration_seconds =19

total_duration = duration_minutes*60+duration_seconds

with open("loop.gpx", "r") as f:
    lines = f.readlines()

timecount = 0
for line in lines:
    if "time" in line:
        timecount += 1

even_increment = 1

time = start_time
intrack = False

def increment_time(time):
    newtime = time + datetime.timedelta(seconds=even_increment)
    return newtime


with open("newtrack.gpx", "w") as f:
    for line in lines:
        if "time" not in line:
            f.write(" "+line)
        elif "time" in line and intrack:
            f.write("        <time>"+time.isoformat()+"Z</time>\n")
            time = increment_time(time)
        else:
            f.write("   <time>"+time.isoformat()+"Z</time>\n")
            intrack = True
