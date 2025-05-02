import pytest

from notes.kleisli_category import compose, safe_reciprocal, safe_sqrt


@pytest.mark.parametrize("value", [x for x in range(-100, 100)])
def test_compose(benchmark, value: int):
    safe_sqrt_reciprocal = compose(safe_sqrt, safe_reciprocal)
    result = benchmark(safe_sqrt_reciprocal, value)
    print(f"{result}")
