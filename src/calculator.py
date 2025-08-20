def addition(a, b):
    """Performs addition of two numbers.

    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.

    Returns:
        int or float: The sum of a and b.

    Examples:
        >>> addition(2, 3)
        5

        >>> addition(2, -4)
        -2

        >>> addition(3.5, 2.1)
        5.6
    """
    return a + b


def substraction(a, b):
    """Performs subtraction of two numbers.

    Args:
        a (int or float): The number from which to subtract.
        b (int or float): The number to subtract.

    Returns:
        int or float: The difference of a minus b.

    Examples:
        >>> substraction(5, 3)
        2

        >>> substraction(10, 15)
        -5

        >>> substraction(7.5, 2.3)
        5.2
    """
    return a - b


def multiplication(a, b):
    """Performs multiplication of two numbers.

    Args:
        a (int or float): The first number to multiply.
        b (int or float): The second number to multiply.

    Returns:
        int or float: The product of a and b.

    Examples:
        >>> multiplication(3, 4)
        12

        >>> multiplication(-2, 5)
        -10

        >>> multiplication(2.5, 4)
        10.0
    """
    return a * b


def division(a, b):
    """Performs division of two numbers.

    Args:
        a (int or float): The dividend (number to be divided).
        b (int or float): The divisor (number to divide by).

    Raises:
        ZeroDivisionError: When attempting to divide by zero.

    Returns:
        float: The quotient of a divided by b.

    Examples:
        >>> division(6, 3)
        2.0

        >>> division(7, 2)
        3.5

        >>> division(6, 0)
        Traceback (most recent call last):
        ZeroDivisionError: Not allowed division by zero
    """
    if b == 0:
        raise ZeroDivisionError("Not allowed division by zero")
    return a / b
