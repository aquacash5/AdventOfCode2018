if __name__ == '__main__':
    # Tests
    assert(sum([1, 1, 1]) == 3)
    assert(sum([1, 1, -2]) == 0)
    assert(sum([-1, -2, -3]) == -6)

    # Solution
    with open('data.txt') as f:
        print(sum(int(i) for i in f))