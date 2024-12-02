import numpy as np

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

def systemof_equations(a1, b1, c1, a2, b2, c2):
    """ solves a system of two linear equations with two unknowns using Cramer Rule

    Args:
        a1 (float): coefficient of x in the first equation (a1 * x + b1 * y = c1)
        b1 (float): coefficient of y in the first equation (a1 * x + b1 * y = c1)
        c1 (float): constant term in the first equation (a1 * x + b1 * y = c1)
        a2 (float): coeffincinent of x in the seconf equation (a2 * x + b2 * y = c2)
        b2 (float): coeffincinent of y in the seconf equation (a2 * x + b2 * y = c2)
        c2 (flaot): constant term in the second equation (a2 * x + b2 * y =c2)

    Raises:
        ValueError: If the determinant of the system is zero, indicating no unique solution

    Returns:
        dict: a dictionary contatining the solution with keys 'X' for the value of x and 'Y' for the value of y
    """
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        raise ValueError("The system has no unique soloution")
    x = (c1 * b2 - c2 * b1) / determinant
    y = (a1 * c2 - a2 * c1) / determinant

    return {'X': x, 'Y':y}


def test_systemof_equations():
    result = systemof_equations(3, 4, 18, 5, -2, 4)
    assert abs(result['X'] - 2) < 1e-5
    assert abs(result['Y'] - 3) < 1e-5

def generate_samples(num_samples, mean, std_dev):
    return np.random.normal(mean, std_dev, num_samples)

def test_generate_samples():
    num_samples = 1000
    mean = 0
    std_dev = 1

    samples = generate_samples (num_samples, mean, std_dev)

    generated_mean = np.mean(samples)
    generated_std_dev = np.std(samples)

    assert abs(generated_mean - mean) < 0.1
    assert abs(generated_std_dev - std_dev) < 0.1


