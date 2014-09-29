__author__ = 'Mamadou'

def fibonacci1(n):
    if(n == 1):
        return 1
    return n + fibonacci1(n-1)

def fibonacci2(n):
  fib_list = [0,1]
  for x in range(0,n):
      while (fib_list[-1]+fib_list[-2] <= n):
        fib_list.append(fib_list[-1]+fib_list[-2])
  print fib_list

def test_fibo1():
    assert fibonacci2(5) == [0,1,1,2,3,5]

#fibonacci1(2000)
#fibonacci2(2)
test_fibo1()