def integrate_linear(a, b, x1 ,x2): 
    """calculates the definite integral of a linear function ax + b over the range
    [x1, x2]

    Args:
        a (float): the coefficient of x in the linear function
        b (float): the constant term in the linear function
        x1 (float): the lower bound og the intefration ranfe
        x2 (float): the upper bound of the integration range

    Returns:
        float: the result of the definite integral of ax + b from x1 to x2
    """
    integral_2x = (a / 2) * (x2 ** 2) + b * x2
    integral_1x = (a / 2) * (x1 ** 2) + b * x1
    return integral_2x - integral_1x

def test_integrate_linear_():
    result = integrate_linear(4, 2, 1, 5)
    assert abs(result - 56.0) < 1e-5 