from math import factorial
is_curious = lambda x: x == sum(map(lambda y: factorial(int(y)), list(str(x))))

# guessing 1mil as upper limit...could prove through analysis, but might as well try
print sum([x for x in xrange(10, 1000000) if is_curious(x)])