digital_sum = lambda x, y: sum([int(i) for i in list(str(x**y))])
print max([digital_sum(a, b) for a in range(1, 100) for b in range(1, 100)])
