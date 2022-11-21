from typing import Callable

import pytest
from fibonacci.dynamic import fibonacci_dynamic, fibonacci_dynamic_v2
from fibonacci.cached import fibonacci_cached, fibonacci_lru_cached
from fibonacci.naive import fibonacci_naive


@pytest.mark.parametrize("n,expected", [(0, 0), (1, 1), (2, 1), (20, 6765)])
@pytest.mark.parametrize(
    "fib_func",
    [
        fibonacci_naive,
        fibonacci_cached,
        fibonacci_lru_cached,
        fibonacci_dynamic,
        fibonacci_dynamic_v2,
    ],
)
def test_fibonacci(
    time_tracker, fib_func: Callable[[int], int], n: int, expected: int
) -> None:
    res = fib_func(n)
    assert res == expected
