def myfunc(n):
  return lambda a: a * n

mydoubler = myfunc(2)

mydoubler = lambda a: a * 2
def mydoubler(a):
    return a*2


print(mydoubler(11))