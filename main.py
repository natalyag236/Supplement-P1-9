def test_integrate_linear_():
    result = integrate_linear_(4, 2, 1, 5)
    assert abs(result - 72.0) < 1e-5 