# letters and values - { 'A': 1, 'B': 2, ... , 'Z': 26 }
vals = dict(zip(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), range(1, 26 + 1)))

# score('HELLO') -> ['H', 'E', 'L', 'L', 'O']
# -> [8, 5, 12, 12, 15] -> 8 + 5 + 12 + 12 + 15 -> 52
score = lambda name: sum(map(lambda x: vals[x], list(name)))

# positional_score((3, 'ABC')) -> 4 * (1 + 2 + 3) -> 24
positional_score = lambda x: (x[0] + 1) * score(x[1])

with open('names.txt', 'r') as f:
  names = sorted(f.read().replace('"', "").split(','))
  print sum(map(positional_score, list(enumerate(names))))
