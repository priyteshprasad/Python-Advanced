import calendar 

# Create a plan text calendar 
c = calendar.TextCalendar(calendar.MONDAY)
str = c.formatmonth(2022, 10, 0, 0)
print(str)

# TODO: Create a HTML formated calendar 
hc = calendar.HTMLCalendar(calendar.SUNDAY)
str = hc.formatmonth(2022, 1)

print(str)

# TODO loop over the days of a month 
#  zeroes mean that hte day of the week is an overlapping month
for i in c.itermonthdays(2022,8):
  print(i)

# TODOThe calendar module provides useful utilities for the given locale 
#such as the name of the days and months in both full and abbreviated form 

for name in calendar.month_name:
  print(name)
for day in calendar.day_name:
  print(day)
  
# Calculate days based on a rule

print("Team meeting will be on:")
for m in range(1,13):
  cal = calendar.monthcalendar(2022, m)
  week1 = cal[0]
  week2  = cal[1]
  if week1[calendar.FRIDAY] != 0:
    meetday = week1[calendar.FRIDAY]
  else:
    meetday = week2[calendar.FRIDAY]
    
  print(calendar.month_name[m], meetday)