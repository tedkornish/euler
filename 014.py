cache = {}

def collatz_len(x):
  current = x
  count = 0
  
  while current != 1:
    if current in cache: return count + cache[current]

    if current % 2 == 0: current /= 2
    else: current = current * 3 + 1
    count += 1

  cache[x] = count
  return count

print "Number and length:"
print max(map(lambda x: [x, collatz_len(x)], range(1, 1000000 + 1)), key=lambda x: x[1])