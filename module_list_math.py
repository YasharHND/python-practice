from functools import reduce


def product(values):
    return reduce(lambda x, y: x * y, values)


def summation(values):
    return sum(values)


def count(values):
    return len(values)
