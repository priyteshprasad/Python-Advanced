# exceptoin handeling

# x = 10/0

try:
  ans = input("divide 100 by: ")
  num = int(ans)
  print(10/num)
except ZeroDivisionError as e:
  print("dividing by zero not allowed")
except ValueError as e:
  print(e, "| Means:that was not a number!")
finally:
  print("this line always gets print")
  