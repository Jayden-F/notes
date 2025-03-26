from typing import Callable, TypeVar
from dataclasses import dataclass


@dataclass
class Ok[T]:
    value: T


@dataclass
class Err[U]:
    error: U


T = TypeVar("T")
U = TypeVar("U")
Result = Ok[T] | Err[U]


def safe_reciprocal(x: float) -> Result[float, list[str]]:
    if x == 0:
        return Err(["Cannot compute recipriocal of Zero"])
    return Ok(1 / x)


def sqrt(x: float) -> float:
    return x ** (1 / 2)


def safe_sqrt(x: float) -> Result[float, list[str]]:
    if x < 0:
        return Err([f"Cannot sqrt a negative number: {x}"])
    return Ok(sqrt(x))


def compose[A, B, C](
    f: Callable[[A], Result[B, list[str]]],
    g: Callable[[B], Result[C, list[str]]],
) -> Callable[[A], Result[C, list[str]]]:
    def result_fn(x: A) -> Result[C, list[str]]:
        p1 = f(x)
        match p1:
            case Err():
                return p1
            case Ok(value=value):
                return g(value)

    return result_fn
