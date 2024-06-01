import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise Exception('Division by 0.')
    return a / b


def power(a, b):
    return a ** b


def square_root(a):
    if a < 0:
        raise Exception('There is no square root from negative number')
    return math.sqrt(a)


def percent(a):
    return a / 100


def factorial(a):
    if a < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if a == 0:
        return 1
    result = 1
    v = int(a + 1)
    for i in range(2, v):
        result *= i
    return result


def sin_angle(x):
    return math.sin(x)


def cos_angle(x):
    return math.cos(x)


def tan_angle(x):
    return math.tan(x)


def ctg_angle(x):
    if math.isclose(math.tan(x), 0, abs_tol=1e-9):
        raise ValueError("Cotangent is undefined for this angle as tangent approaches zero.")
    return 1 / math.tan(x)
