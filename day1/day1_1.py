total = 0
with open('data.txt') as f:
    for i in f:
        total += int(i)
print(total)
