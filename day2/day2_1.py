from collections import defaultdict


def checksum(iterator):
    totals = defaultdict(int)
    for data in iterator:
        t = set()
        d = set(data)
        for a in d:
            t.add(data.count(a))
        for k in t:
            totals[k] += 1
    return totals[2] * totals[3]


if __name__ == '__main__':
    # Tests
    data = ['abcdef', 'bababc', 'abbcde',
            'abcccd', 'aabcdd', 'abcdee', 'ababab']
    assert(checksum(data) == 12)

    # Solution
    with open('data.txt') as f:
        print(checksum(f))
