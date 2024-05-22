def fibonacci(n):
    """
    Calculate the nth Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to calculate.

    Returns:
        int: The nth Fibonacci number.

    Example:
         >>> fibonacci(5)
        3

    Description:
        This function calculates the nth Fibonacci number using an iterative approach.
        It starts with the base case of 0 and 1, then iteratively applies the recurrence relation
        to generate the next number in the sequence.

    :param n: The position of the Fibonacci number to calculate.
    :return: The nth Fibonacci number.
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def merge_sorted_lists(left_list: list, right_list: list) -> list:
    """Merge two sorted lists into one sorted list.

    This function takes two sorted lists as input and returns a new sorted list
    that is the result of merging the two input lists. The resulting list is
    also sorted in ascending order.

    Args:
        left_list (list): The first sorted list.
        right_list (list): The second sorted list.

    Returns:
        list: A new sorted list that is the result of merging the two input lists.

    Example:
         >>> left_list = [1, 3, 5]
         >>> right_list = [2, 4, 6]
         >>> merge_sorted_lists(left_list, right_list)
         [1, 2, 3, 4, 5, 6]

    :author: Senior Python Developer
    :goal: To review Python functions and ensure that variable names are following best practices.
    """
    result = []
    list_index_left, list_index_right = 0, 0
    while list_index_left < len(left_list) and list_index_right < len(right_list):
        if left_list[list_index_left] < right_list[list_index_right]:
            result.append(left_list[list_index_left])
            list_index_left += 1
        else:
            result.append(right_list[list_index_right])
            list_index_right += 1
    result.extend(left_list[list_index_left:])
    result.extend(right_list[list_index_right:])
    return result

