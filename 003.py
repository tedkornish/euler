from math import sqrt, ceil

int_ceil_sqrt = ics = lambda x: int(ceil(sqrt(x)))

def factors(x):
  f = []
  for i in xrange(1, ics(x) + 1):
    if x % i == 0:
      f.append(i)
      f.append(x / i)
  return sorted(list(set(f)))

def is_prime(x):
  if x == 1: return False
  elif x == 2 or x == 3: return True
  for i in xrange(2, ics(x) + 1):
    if x % i == 0:
      return False
  return True

prime_factors = lambda x: [i for i in factors(x) if is_prime(i)]

print max(prime_factors(600851475143))