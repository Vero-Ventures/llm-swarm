def factorial(n):
    """
    Calculates the factorial of a non-negative integer using recursion.

    Args:
        n (int): The non-negative integer whose factorial is to be calculated.

    Returns:
        int: The factorial of the input integer.

    Raises:
        ValueError: If the input is a negative integer.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)