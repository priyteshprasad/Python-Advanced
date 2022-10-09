import os 
from os import path
import datetime
from datetime import date, time, timedelta
import time 


def main():
  # print name of operating system
  print(os.name)
  
  # check for itemexistance and type
  print("Item exists:", str(path.exists("textfile.txt")))
  print("Item is a file:", path.isfile("textfile.txt"))
  print("Item is a directory:", path.isdir("textfile.txt"))  

  # working with file paths
  print("Items'path:", path.realpath("textfile.txt"))
  print("Item's path and name", path.split(path.realpath("textfile.txt")))

  # get the modification time
  t = time.ctime(path.getmtime("textfile.txt")) # ctime-> convert to readable time
  print(t)
  print(datatime.datatime.fromtimestamp(path.getmtime(path.split(path.realpath("textfile.txt")[1]))))



if __name__ == "__main__":
  main()