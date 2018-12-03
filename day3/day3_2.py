from collections import defaultdict


def coverage(data):
    sheet = defaultdict(list)
    ids = set()
    for segment in data:
        num, _, pos, size = segment.lstrip('#').split(' ')
        left, top = pos.rstrip(':').split(',')
        x_, y_ = size.split('x')
        left, top, x_, y_ = int(left), int(top), int(x_), int(y_)
        ids.add(num)
        for x in range(left, left + x_):
            for y in range(top, top + y_):
                sheet[f'{x},{y}'].append(num)
    bad_segments = set()
    for i in sheet.values():
        if len(i) > 1:
            for j in i:
                bad_segments.add(j)
    return (ids - bad_segments).pop()


if __name__ == '__main__':
    # Tests
    data = [
        '#1 @ 1,3: 4x4',
        '#2 @ 3,1: 4x4',
        '#3 @ 5,5: 2x2'
    ]
    assert(coverage(data) == '3')

    # Solution
    with open('data.txt') as f:
        print(coverage(list(f)))
