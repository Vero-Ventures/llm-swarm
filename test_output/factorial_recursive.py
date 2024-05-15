def factorial_recursive(n: int):
    if n < 0:
        raise ValueError("Input should be a non-negative integer")
    elif n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)