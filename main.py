def test_integrate_linear_():
    result = integrate_linear(4, 2, 1, 5)
    assert abs(result - 56.0) < 1e-5 