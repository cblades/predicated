from umpie import Predicate, gt, contains


@Predicate
def foo(x: int) -> bool:
    """Return True if x is greater than 0"""
    return x > 0


def bar(x: int) -> bool:
    """Return True if x is less than 10"""
    return x < 10


c = foo & bar & gt(2)


print(contains(4)([1, 2, 3]))
