from notes.kleisli_category import compose, safe_reciprocal, safe_sqrt


def test_compose():
    safe_sqrt_reciprocal = compose(safe_sqrt, safe_reciprocal)

    for i in range(-100, 100):
        print(safe_sqrt_reciprocal(i))
