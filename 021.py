from math import sqrt, ceil

int_ceil_sqrt = ics = lambda x: int(ceil(sqrt(x)))

def factors(x):
  f = []
  for i in xrange(1, ics(x) + 1):
    if x % i == 0:
      f.append(i)
      f.append(x / i)
  return sorted(list(set(f)))

sum_factors = lambda x: sum(factors(x)[:-1])

def is_amicable(x):
  a = sum_factors(x)
  b = sum_factors(a)
  return a != b and b == x

print sum([x for x in range(1, 10000 + 1) if is_amicable(x)])