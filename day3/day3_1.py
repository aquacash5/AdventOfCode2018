from collections import defaultdict


def coverage(data):
    sheet = defaultdict(int)
    for segment in data:
        _, _, pos, size = segment.split(' ')
        left, top = pos.rstrip(':').split(',')
        x_, y_ = size.split('x')
        left, top, x_, y_ = int(left), int(top), int(x_), int(y_)
        for x in range(left, left + x_):
            for y in range(top, top + y_):
                sheet[f'{x},{y}'] += 1
    return len([i for i in sheet.values() if i > 1])


if __name__ == '__main__':
    # Tests
    data = [
        '#1 @ 1,3: 4x4',
        '#2 @ 3,1: 4x4',
        '#3 @ 5,5: 2x2'
    ]
    assert(coverage(data) == 4)

    # Solution
    with open('data.txt') as f:
        print(coverage(f))
