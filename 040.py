from operator import mul

root_num = ''
counter = 1
while True:
  root_num += str(counter)
  counter += 1
  if len(root_num) > 1000000:
    break

digits = list(root_num)
print reduce(mul, [int(digits[10 ** i - 1]) for i in range(0, 6 + 1)])
