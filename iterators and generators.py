'''
Iterable - __itor and __getItem is defined
Iterator - next element is defined
Iteration - kisi k next element ko fetch karte jaana
generator - value can be generate one time 

'''
def gen(n):
  for i in range(n):
    yield i
    
ob1 = gen(1000)
# print(next(ob1))
# print(next(ob1))
# print(next(ob1))
# print(next(ob1))
# for i in gen(1000):
#   print(i)

def fib(limit):
  a, b = 0, 1 
  while a < limit:
    yield a 
    b, a = a + b, b 
    
x = fib(16)
print(x)
for i in x:
  print (i)