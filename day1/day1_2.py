from itertools import cycle

current_total = 0
totals = set([0])

with open('data.txt') as f:
    data = [int(i) for i in f]

for i in cycle(data):
    current_total += int(i)
    if current_total in totals:
        break
    else:
        totals.add(current_total)
print(current_total)
