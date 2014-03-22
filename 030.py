sum_of_fifth = lambda x: sum(map(lambda y: int(y)**5, list(str(x))))

counter = 0
for i in xrange(2, 1000000): # just a guess...final # is probably less than 1mil
  if sum_of_fifth(i) == i: counter += i

print counter