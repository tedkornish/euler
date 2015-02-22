def palindrome(num):
  s = str(num)
  return len(s) < 2 or (s[0] == s[-1] and palindrome(s[1:-1]))

binString = lambda num: bin(num)[2:]
pals = lambda num: palindrome(num) and palindrome(binString(num))

print sum(filter(pals, range(1, 1000000)))
