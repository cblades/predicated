from umpie import Predicate

__all__ = ["contains", "gt", "lt", "eq", "ne", "ge", "le"]


def contains(x) -> Predicate:
    return Predicate(
        lambda y: x in y,
        __doc__=f"Return True if {x} is in y",
        __name__=f"contains_{x}",
        __repr__=f"contains({x})",
    )


def gt(x) -> Predicate:
    return Predicate(
        lambda y: y > x,
        __doc__=f"Return True if x > {x}",
        __name__=f"gt_{x}",
        __repr__=f"gt({x})",
    )


def lt(x) -> Predicate:
    return Predicate(
        lambda y: y < x,
        __doc__=f"Return True if x < {x}",
        __name__=f"lt_{x}",
        __repr__=repr(f"lt({x})"),
    )


def eq(x) -> Predicate:
    return Predicate(
        lambda y: y == x,
        __doc__=f"Return True if x == {x}",
        __name__=f"eq_{x}",
        __repr__=f"eq({x})",
    )


def ne(x) -> Predicate:
    return Predicate(
        lambda y: y != x,
        __doc__=f"Return True if x != {x}",
        __name__=f"ne_{x}",
        __repr__=f"ne({x})",
    )


def ge(x) -> Predicate:
    return Predicate(
        lambda y: y >= x,
        __doc__=f"Return True if x >= {x}",
        __name__=f"ge_{x}",
        __repr__=f"ge({x})",
    )


def le(x) -> Predicate:
    return Predicate(
        lambda y: y <= x,
        __doc__=f"Return True if x <= {x}",
        __name__=f"le_{x}",
        __repr__=f"le({x})",
    )
