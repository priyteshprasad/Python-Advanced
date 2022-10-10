from datetime import date 
from datetime import time 
from datetime import datetime 
from datetime import timedelta #amount of time


# TODO: construct a basic timedelta and print it 
print(timedelta(days=365, hours=5, minutes=1))

# TODO: print todays date 
now = datetime.now()
print("Today is", now)

# TODO: print today's date one year from now
print("one year from now it will be",str(now + timedelta(days=365)))

# TODO: create a timedelta that uses more than one argument
print("In two weeks and 3 days, it will be", str(now + timedelta(weeks=2, days= 3)))

# TODO: calculate the date 1 week ago, formatted as string 
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print("One week ago it was", s)


# TODO: how many days it is till nwext april fools days
today = date.today()
afd = date(today.year, 4, 1) 

# 
if afd < today:
  print("april fools day already wet by:", ((today - afd).days))
  
  afd = afd.replace(year = today.year + 1)
  
time_to_afd = afd - today
print("It is ", time_to_afd.days, " days until the next April Fools Day!")




