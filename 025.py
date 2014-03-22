def fib():
  a, b = 0, 1
  while True:
    yield b
    a, b = b, a + b

seq = fib()

counter = 1
current = seq.next()

while len(str(current)) < 1000:
  current = seq.next()
  counter += 1

print counter