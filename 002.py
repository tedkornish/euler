def fib():
  a, b = 0, 1
  while True:
    yield b
    a, b = b, a + b

seq = fib()

counter = 0
while True:
  current = seq.next()
  if current % 2 == 0: counter += current
  if current > 4000000: break

print counter