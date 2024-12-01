def integrate_linear(a, b, x1 ,x2): 
    integral_2x = (a / 2) * (x2 ** 2) + b * x2
    integral_1x = (a / 2) * (x1 ** 2) + b * x1
    return integral_2x - integral_1x

def test_integrate_linear_():
    result = integrate_linear(4, 2, 1, 5)
    assert abs(result - 56.0) < 1e-5 