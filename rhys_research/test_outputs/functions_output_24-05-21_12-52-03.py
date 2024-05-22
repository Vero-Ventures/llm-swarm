def fibonacci(n):
    """Compute the `n`-th Fibonacci number.

    The Fibonacci sequence is a series of numbers where each subsequent
    number is the sum of the previous two. This function returns the
    `n`-th number in this sequence, starting from 0 and 1 (the traditional
    starting points).

    Parameters:
        n (int): The index of the Fibonacci number to compute.

    Returns:
        int: The `n`-th Fibonacci number.

    Example:
         >>> fibonacci(5)
        3

    Note:
        This function uses an iterative approach to calculate the
        Fibonacci sequence. It is not suitable for large values of `n`,
        as its time complexity is O(n)."""
    first_value, second_value = 0, 1
    for _ in range(n):
        first_value, second_value = second_value, first_value + second_value
    return first_value

def merge_sorted_lists(left_list: list, right_list: list) -> list:
    """Merges two sorted lists into a single sorted list.
    
    Args:
        left_list (list): The first sorted list.
        right_list (list): The second sorted list.
    
    Returns:
        list: A single sorted list containing all elements from the input lists.
    
    Example:
        >>> left_list = [1, 3, 5, 7]
        >>> right_list = [2, 4, 6, 8]
        >>> merge_sorted_lists(left_list, right_list)
        [1, 2, 3, 4, 5, 6, 7, 8]
    
    Description:
        This function merges two sorted lists into a single sorted list. It compares elements from the two lists and adds them to the result list in order. If one list is exhausted before the other, it appends all remaining elements from the non-exhausted list.
    """
    result = []
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left_list) and right_cursor < len(right_list):
        if left_list[left_cursor] < right_list[right_cursor]:
            result.append(left_list[left_cursor])
            left_cursor += 1
        else:
            result.append(right_list[right_cursor])
            right_cursor += 1
    result.extend(left_list[left_cursor:])
    result.extend(right_list[right_cursor:])
    return result

