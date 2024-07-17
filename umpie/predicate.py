from inspect import signature
from typing import Callable, Generic, TypeVar

V = TypeVar("V")


class Predicate(Generic[V]):
    def __init__(
        self,
        fn: Callable[[V], bool],
        /,
        __doc__=None,
        __name__=None,
        __repr__=None,
        __signature__=None,
    ) -> None:
        if not callable(fn):
            raise TypeError(f"{fn} is not callable")

        if isinstance(fn, Predicate):
            fn = fn.__wraps__

        if len(signature(fn).parameters) > 1:
            raise ValueError(f"{fn} must have only one parameter")

        self.__wraps__ = fn
        self.__doc__ = __doc__ or self.__wraps__.__doc__
        self.__name__ = __name__ or self.__wraps__.__name__
        self._repr = (
            __repr__ or f"{self.__class__.__name__}({self.__wraps__.__qualname__})"
        )
        self.__signature__ = __signature__ or signature(self.__wraps__)

    def __call__(self, value: V) -> bool:
        return self.__wraps__(value)

    def __and__(self, other: Callable[[V], bool]) -> "Predicate[V]":
        other_fn = other.__wraps__ if isinstance(other, Predicate) else other

        def _and(value: V) -> bool:
            return self(value) and other_fn(value)

        __name__ = f"{self.__name__}_and_{other.__name__}"

        param_name = next(iter(self.__signature__.parameters.keys()))
        __doc__ = f"{self.__wraps__.__name__}({param_name}) and {other_fn.__name__}({param_name})\n\n"

        docs = [
            f"{d.__name__}\n\t{d.__doc__}"
            for d in (self.__wraps__, other_fn)
            if d.__doc__
        ]

        __doc__ += "\n\n".join(docs)

        class_name = self.__class__.__name__
        return Predicate(
            _and,
            __doc__,
            __name__,
            __repr__=f"{class_name}({self.__wraps__.__name__}) and {class_name}({other_fn.__name__})",
            __signature__=self.__signature__,
        )

    def __rand__(self, other: Callable[[V], bool]) -> "Predicate[V]":
        return Predicate(other) & self

    def __repr__(self) -> str:
        return self._repr
