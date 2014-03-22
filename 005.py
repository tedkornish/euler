def divisible(x):
  for i in xrange(1, 21):
    if x % i != 0:
      return False
  return True

current = 20

while not divisible(current): current += 20
print current