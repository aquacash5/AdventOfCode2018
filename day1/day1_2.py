from itertools import cycle


def find_frequency(iterator):
    frequency = 0
    seen = {0}
    for i in cycle(iterator):
        frequency += int(i)
        if frequency in seen:
            return frequency
        else:
            seen.add(frequency)


if __name__ == '__main__':
    # Tests
    assert(find_frequency([1, -1]) == 0)
    assert(find_frequency([3, 3, 4, -2, -4]) == 10)
    assert(find_frequency([-6, 3, 8, 5, -6]) == 5)
    assert(find_frequency([7, 7, -2, -7, -4]) == 14)

    # Solution
    with open('data.txt') as f:
        print(find_frequency(int(i) for i in f))
