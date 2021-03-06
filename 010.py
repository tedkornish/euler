from math import sqrt, ceil

int_ceil_sqrt = ics = lambda x: int(ceil(sqrt(x)))

def is_prime(x):
  if x == 1: return False
  elif x == 2 or x == 3: return True
  for i in xrange(2, ics(x) + 1):
    if x % i == 0:
      return False
  return True

print sum([x for x in range(1, 2000000) if is_prime(x)])