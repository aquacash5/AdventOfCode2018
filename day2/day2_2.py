def differance(a, b):
    alt = ''
    for c, d in zip(a, b):
        if c == d:
            alt += c
    return alt


def off_by_1(data):
    while data:
        first = data.pop()
        for d in data:
            diff = differance(first, d)
            if len(first) - len(diff) == 1:
                break
        else:
            continue
        break
    return diff


if __name__ == '__main__':
    # Tests
    data = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']
    assert(off_by_1(data) == 'fgij')

    # Solution
    with open('data.txt') as f:
        print(off_by_1(list(f)))
