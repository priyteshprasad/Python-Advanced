from datetime import datetime

def add(a, b):
  return a + b
  
def main():
  # Times and Date can be formatted using a set of predefined string
  # control codes 
  now = datetime.now()
  
  # ###Date Formatting
  
  # %y/%Y -Year, %a/%A - weekday, %b/%B-month, %d-day of month 
  print(now.strftime("The current year is: %Y"))
  print(now.strftime("%a, %d %B, %y"))
  
  
  # %c - locale's date and time, %x - locale's date, %X - locale's time
  print(now.strftime("Local date and time: %c"))
  print(now.strftime("Local date: %x"))
  print(now.strftime("Local time: %X"))
  
  # ###Time Formating ###
  # %I/%H -12/24 Hour, %M -minute, %S -second, %p- locale' AM/PM 
  print(now.strftime("Current time: %I:%M:%S %p"))
  print(now.strftime("24 hour time: %H:%M:%S %p"))
  
if __name__ == '__main__':
  main()