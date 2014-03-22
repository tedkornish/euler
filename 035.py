from collections import deque
from math import sqrt, ceil

int_ceil_sqrt = ics = lambda x: int(ceil(sqrt(x)))

def is_prime(x):
  if x == 1: return False
  elif x == 2 or x == 3: return True
  for i in xrange(2, ics(x) + 1):
    if x % i == 0:
      return False
  return True

def is_circular(x):
  d = deque(list(str(x)))
  for i in xrange(len(str(x))):
    if not is_prime(int("".join(d))): return False
    d.rotate(1)
  return True

primes = [x for x in xrange(1, 1000000) if is_circular(x)]
print len(primes)