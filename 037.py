from math import sqrt, ceil

int_ceil_sqrt = ics = lambda x: int(ceil(sqrt(x)))
num = lambda x: int("".join(x))

def is_prime(x):
  if x == 1: return False
  elif x == 2 or x == 3: return True
  for i in xrange(2, ics(x) + 1):
    if x % i == 0:
      return False
  return True

def is_truncatable(x):
  orig = list(str(x))

  if not is_prime(x): return False

  for i in xrange(len(orig)-1):
    current = num(orig[:-1 * i - 1])
    if not is_prime(current): return False

  for i in xrange(len(orig)-1):
    current = num(orig[-1 * i - 1:])
    if not is_prime(current): return False

  return True

# again, guessing at 1mil for the limit...
print sum([x for x in range(10, 1000000 + 1) if is_truncatable(x)])