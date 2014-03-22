from math import sqrt, ceil

int_ceil_sqrt = ics = lambda x: int(ceil(sqrt(x)))

def is_prime(x):
  if x == 1: return False
  elif x == 2 or x == 3: return True
  for i in xrange(2, ics(x) + 1):
    if x % i == 0:
      return False
  return True

counter = 0
current = 0

while counter != 10001:
  current += 1
  if is_prime(current): counter += 1

print current