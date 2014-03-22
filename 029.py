terms = []
for i in range(2, 100 + 1):
  for j in range(2, 100 + 1):
    terms.append(i ** j)

print len(set(terms))