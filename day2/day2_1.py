from collections import defaultdict

totals = defaultdict(int)

with open('data.txt') as f:
    for data in f:
        t = set()
        d = set(data)
        for a in d:
            t.add(data.count(a))
        for k in t:
            totals[k] += 1
print(totals[2] * totals[3])
