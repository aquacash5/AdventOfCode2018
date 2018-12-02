def differance(a, b):
    alt = ''
    for c, d in zip(a, b):
        if c == d:
            alt += c
    return alt


with open('data.txt') as f:
    data = [i for i in f]

while data:
    first = data.pop()
    for d in data:
        diff = differance(first, d)
        if len(first) - len(diff) == 1:
            break
    else:
        continue
    break
print(diff)
