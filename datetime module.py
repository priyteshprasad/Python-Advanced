import datetime
from datetime import date 
from datetime import time 
from datetime import datetime



def main():
  # Date Object 
  # TODO: get today's date from the stamp today() method from the datetime class 
  today = date.today()
  print("Today's date is: ", today)
  
  # TODO: print out the date's individual component 
  print("Date components: ", today.day, today.year, today.month)
  
  # TODO: retrive today's weekday (0=Monday, 6=Sunday)
  print("Today's weekday no. is :", today.weekday())
  days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  print("which is a", days[today.weekday()])
  
  ## Datetime Object
  # TODO: Get today's date from the datetime class 
  today = datetime.now()
  print("The current date and time is ", today )
  
  # TODO: Get the current time
  t = datetime.time(datetime.now())
  print("The current time is,", t)
  
  
  
  
if __name__ == '__main__':
  main()