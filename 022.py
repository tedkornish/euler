vals = dict(zip(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), range(1, 26 + 1)))
score = lambda name: sum(map(lambda x: vals[x], list(name)))
positional_scorer = lambda x: (x[0] + 1) * score(x[1])

with open('names.txt', 'r') as f:
  names = sorted(f.read().replace('"', "").split(','))
  print sum(map(positional_scorer, list(enumerate(names))))