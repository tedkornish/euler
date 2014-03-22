def is_palindrome(x):
  str_arr = list(str(x))
  l = len(str_arr)/2 # int
  for i in xrange(l):
    if str_arr[i] != str_arr[-1 * (i+1)]: return False
  return True

current = 0 # current max
a, b = 999, 999

# Iterate down for a
# When a * b is less than current max, decrement b and reset a to 999
# Finish when b is less than 100

while b > 99:
  product = a * b
  if product < current:
    a, b = 999, b-1
  else:
    if is_palindrome(product): current = product
    a -= 1

print current