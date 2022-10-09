# basic file operation

def main():
  myfile = open("textfile.txt", "w+") #w means we will be able to write and + means python should make the file if not already existing
  # myfile = open("textfile.txt", "a+") #a means append(without overrwriting)
  for i in range(10):
    myfile.write("this is some new text\n")
    
  myfile.close() # close if you are writting
  
  myfile = open("textfile.txt", "r")
  if myfile.mode == 'r':
    content = myfile.read()
    print(content)
    
  if myfile.mode == 'r':
    fl = myfile.readlines()
    for x in fl:
      print(x)

if __name__ == "__main__":
  main()
  
  